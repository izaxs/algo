# Implement a Key value store that supports nested transactions.

# Transactions: begin/commit/rollback
# Commit or rollback outer transaction implicitly commit or rollback all inner transactions

from __future__ import annotations

# KVStore supports Python's with statement
class KVStore:
    def __init__(self):
        self.data: dict[str, int] = {}
        self.layers: list[Transaction] = []

    def _exists(self, transaction: Transaction) -> bool:
        for t in reversed(self.layers):
            if t is transaction: return True
        return False

    def begin(self) -> Transaction:
        transaction = Transaction(self)
        if self.layers:
            self.layers[-1].assertNotClosed()
        self.layers.append(transaction)
        return transaction

    def commit(self, target: Transaction):
        if not self._exists(target): return
        for i in range(len(self.layers)-1, -1, -1):
            curTransaction = self.layers[i]
            if curTransaction.closed: continue
            outer: Transaction | dict[str, int] = self.data
            if i > 0:
                outer = self.layers[i-1]
                if outer.closed: 
                    curTransaction.closed = True
                    continue
            for key, value in curTransaction:
                outer[key] = value
            curTransaction.closed = True
            if curTransaction is target:
                self.layers = self.layers[:i]
                break

    def rollback(self, transaction: Transaction):
        if not self._exists(transaction): return
        for i in range(len(self.layers)-1, -1, -1):
            curTransaction = self.layers[i]
            if curTransaction.closed: continue
            curTransaction.closed = True
            if curTransaction is transaction:
                self.layers = self.layers[:i]
                break

    def contains(self, key):
        for transaction in reversed(self.layers):
            if key in transaction:
                transaction.assertNotClosed()
                return True
        return key in self.data

    def get(self, key):
        for transaction in reversed(self.layers):
            if key in transaction:
                transaction.assertNotClosed()
                return transaction[key]
        return self.data[key]

    def set(self, key, value):
        if not self.layers:
            self.data[key] = value
            return
        target = self.layers[-1]
        target.assertNotClosed()
        target[key] = value

    def delete(self, key):
        if not self.layers:
            del self.data[key]
            return
        target = self.layers[-1]
        target.assertNotClosed()
        del target[key]

class Transaction:
    def __init__(self, store: KVStore):
        self.store = store
        self._data: dict[str, int] = {}
        self.closed: bool = False

    def __iter__(self):
        yield from self._data.items()

    def __setitem__(self, key, value):
        self.assertNotClosed()
        self._data[key] = value

    def __getitem__(self, key) -> int:
        self.assertNotClosed()
        return self._data[key]
    
    def __delitem__(self, key):
        self.assertNotClosed()
        del self._data[key]
    
    def __contains__(self, key) -> bool:
        self.assertNotClosed()
        return key in self._data
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()

    def assertNotClosed(self):
        if self.closed:
            raise ValueError(self.TRANSACTION_CLOSED_ERROR)

    def commit(self):
        self.store.commit(self)

    def rollback(self):
        self.store.rollback(self)

    def set(self, key, value):
        self[key] = value

    def get(self, key) -> int:
        return self[key]

    def delete(self, key):
        del self[key]

    TRANSACTION_CLOSED_ERROR = 'Transaction already closed'

# SimpleKVStore doesn't support multi-thread
class SimpleKVStore:
    def __init__(self):
        self.data = {}
        self.transactions = []
        self.current = 0

    def begin(self):
        self.transactions.append({})

    def rollback(self):
        self.transactions.pop()

    def commit(self):
        for key, value in self.transactions[-1].items():
            self.data[key] = value
        self.transactions.pop()

    def set(self, key, value):
        if not self.transactions:
            self.data[key] = value
        else:
            self.transactions[-1][key] = value

    def get(self, key):
        for transaction in reversed(self.transactions):
            if key in transaction:
                return transaction[key]
        return self.data[key]

    def delete(self, key):
        self.transactions[-1][key] = None

def test_SimpleKVStore():
    store = SimpleKVStore()
    store.set('a', 1)
    store.set('b', 2)
    assert store.get('a') == 1
    assert store.get('b') == 2

    store.begin()
    store.set('a', 11)
    store.set('c', 33)
    assert store.get('a') == 11
    assert store.get('b') == 2
    assert store.get('c') == 33
    store.commit()
    assert store.get('a') == 11
    assert store.get('b') == 2
    assert store.get('c') == 33

    store.begin()
    store.set('a', 111)
    store.set('b', 222)
    store.set('c', 333)
    store.set('d', 444)
    assert store.get('a') == 111
    assert store.get('b') == 222
    assert store.get('c') == 333
    store.rollback()
    assert store.get('a') == 11
    assert store.get('b') == 2
    assert store.get('c') == 33
    assert 'd' not in store.data
    print(f'{test_SimpleKVStore.__name__}() succeed')

def test_KVStore_get_and_set():
    store = KVStore()
    store.set('a', 1)
    store.set('b', 2)
    store.set('b', 3)
    assert store.get('a') == 1
    assert store.get('b') == 3
    print(f'{test_KVStore_get_and_set.__name__}() succeed')

def test_KVStore_single_transaction_commit_implict():
    store = KVStore()
    with store.begin() as t:
        t.set('a', 1)
        t.set('b', 2)
        assert t.get('a') == 1
        assert t.get('b') == 2
        t.set('b', 3)
        assert t.get('b') == 3
    try:
        t.get('a')
        raise ValueError('Should not reach here')
    except ValueError as e:
        assert str(e) == Transaction.TRANSACTION_CLOSED_ERROR
    try:
        t.set('a', 10)
        raise ValueError('Should not reach here')
    except ValueError as e:
        assert str(e) == Transaction.TRANSACTION_CLOSED_ERROR
    assert store.get('a') == 1
    assert store.get('b') == 3
    print(f'{test_KVStore_single_transaction_commit_implict.__name__}() succeed')

def test_KVStore_single_transaction_commit_explicit():
    store = KVStore()
    store.set('a', 0)
    with store.begin() as t:
        t.set('a', 1)
        t.set('b', 2)
        assert t.get('a') == 1
        assert t.get('b') == 2
        t.set('b', 3)
        assert t.get('b') == 3
        t.commit()
    try:
        t.get('a')
        raise ValueError('Should not reach here')
    except ValueError as e:
        assert str(e) == Transaction.TRANSACTION_CLOSED_ERROR
    try:
        t.set('a', 10)
        raise ValueError('Should not reach here')
    except ValueError as e:
        assert str(e) == Transaction.TRANSACTION_CLOSED_ERROR
    assert store.get('a') == 1
    assert store.get('b') == 3
    print(f'{test_KVStore_single_transaction_commit_explicit.__name__}() succeed')

def test_KVStore_single_transaction_store_set_within_transaction_block():
    store = KVStore()
    store.set('a', 0)
    with store.begin() as t:
        store.set('a', -1)
        assert t.get('a') == -1
        assert store.get('a') == -1

        t.set('a', 1)
        t.set('b', 2)
        assert t.get('a') == 1
        assert t.get('b') == 2
        assert store.get('a') == 1
        assert store.get('b') == 2
        t.set('b', 3)
        assert t.get('b') == 3
        assert store.get('b') == 3

        t.commit()
        store.set('a', 10)
        store.set('c', 4)
    assert store.get('a') == 10
    assert store.get('b') == 3
    assert store.get('c') == 4
    print(f'{test_KVStore_single_transaction_commit_explicit.__name__}() succeed')

def test_KVStore_single_transaction_rollback_explicit():
    store = KVStore()
    store.set('a', 0)
    with store.begin() as t:
        t.set('a', 1)
        t.set('b', 2)
        assert t.get('a') == 1
        assert t.get('b') == 2
        t.set('b', 3)
        assert t.get('b') == 3
        t.rollback()
    try:
        t.get('a')
        raise ValueError('Should not reach here')
    except ValueError as e:
        assert str(e) == Transaction.TRANSACTION_CLOSED_ERROR
    try:
        t.set('a', 10)
        raise ValueError('Should not reach here')
    except ValueError as e:
        assert str(e) == Transaction.TRANSACTION_CLOSED_ERROR
    assert store.get('a') == 0
    assert not store.contains('b')
    print(f'{test_KVStore_single_transaction_rollback_explicit.__name__}() succeed')

def test_KVStore_single_transaction_rollback_implicit():
    store = KVStore()
    try:
        store.set('a', 0)
        with store.begin() as t:
            t.set('a', 1)
            t.set('b', 2)
            assert t.get('a') == 1
            assert t.get('b') == 2
            t.set('b', 3)
            assert t.get('b') == 3
            raise SystemExit()
    except SystemExit:
        assert store.get('a') == 0
        assert not store.contains('b')
        print(f'{test_KVStore_single_transaction_rollback_implicit.__name__}() succeed')

def test_KVStore_nested_transaction_commit_implict():
    store = KVStore()
    with store.begin() as t1:
        t1.set('a', 1)
        t1.set('b', 2)
        assert t1.get('a') == 1
        assert t1.get('b') == 2
        with store.begin() as t2:
            t2.set('b', 22)
            assert t2.get('b') == 22
        assert t1.get('b') == 22
        t1.set('b', 3)
        assert t1.get('b') == 3
    assert store.get('a') == 1
    assert store.get('b') == 3
    print(f'{test_KVStore_nested_transaction_commit_implict.__name__}() succeed')

def test_KVStore_nested_transaction_commit_outer_early_explicit():
    store = KVStore()
    with store.begin() as t1:
        t1.set('a', 1)
        t1.set('b', 2)
        assert t1.get('a') == 1
        assert t1.get('b') == 2
        with store.begin() as t2:
            t2.set('b', 22)
            assert t2.get('b') == 22
            t1.commit()
        try:
            assert t1.get('b') == 22
            raise ValueError('should not reach here')
        except ValueError as e:
            assert str(e) == t1.TRANSACTION_CLOSED_ERROR
        assert store.get('b') == 22
        try:
            t1.set('b', 3)
            raise ValueError('should not reach here')
        except ValueError as e:
            assert str(e) == t1.TRANSACTION_CLOSED_ERROR
    assert store.get('a') == 1
    assert store.get('b') == 22
    print(f'{test_KVStore_nested_transaction_commit_outer_early_explicit.__name__}() succeed')

def test_KVStore_nested_transaction_rollback_inner_explicit():
    store = KVStore()
    with store.begin() as t1:
        t1.set('a', 1)
        t1.set('b', 2)
        assert t1.get('a') == 1
        assert t1.get('b') == 2
        with store.begin() as t2:
            t2.set('b', 22)
            assert t2.get('b') == 22
            t2.rollback()
        try:
            assert t2.get('b') == 2
            raise ValueError('should not reach here')
        except ValueError as e:
            assert str(e) == t2.TRANSACTION_CLOSED_ERROR
        assert t1.get('b') == 2
        t1.set('b', 3)
        assert t1.get('b') == 3
    assert store.get('a') == 1
    assert store.get('b') == 3
    print(f'{test_KVStore_nested_transaction_rollback_inner_explicit.__name__}() succeed')

def test_KVStore_nested_transaction_rollback_inner_implicit():
    store = KVStore()
    try:
        store.set('a', 0)
        with store.begin() as t1:
            t1.set('a', 1)
            t1.set('b', 2)
            assert t1.get('a') == 1
            assert t1.get('b') == 2
            with store.begin() as t2:
                t2.set('b', 22)
                assert t2.get('b') == 22
                raise SystemExit()
    except SystemExit:
        assert store.get('a') == 0
        assert not store.contains('b')
        print(f'{test_KVStore_nested_transaction_rollback_inner_implicit.__name__}() succeed')

if __name__ == '__main__':
    test_SimpleKVStore()
    test_KVStore_get_and_set()
    test_KVStore_single_transaction_commit_implict()
    test_KVStore_single_transaction_commit_explicit()
    test_KVStore_single_transaction_store_set_within_transaction_block()
    test_KVStore_single_transaction_rollback_explicit()
    test_KVStore_single_transaction_rollback_implicit()
    test_KVStore_nested_transaction_commit_implict()
    test_KVStore_nested_transaction_commit_outer_early_explicit()
    test_KVStore_nested_transaction_rollback_inner_explicit()
    test_KVStore_nested_transaction_rollback_inner_implicit()
