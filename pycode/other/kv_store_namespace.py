import pickle

class Data:
    ALWAYS_VALID = -1
    # ttl is treated as exclusive: [)
    def __init__(self, value: str, ts: str = '', ttl: str = ''):
        self.value = value
        self.expireAt = int(ts) + int(ttl) if ts and ttl else self.ALWAYS_VALID

    def isActive(self, ts: str) -> bool:
        if self.expireAt == self.ALWAYS_VALID: return True
        return int(ts) < self.expireAt

# Assume query timestamp came in order
# Otherwise, we need to keep a version history
class KVStore:
    OK = 'true'
    FAILED = 'false'

    def __init__(self):
        self.emptyData = Data('')
        self.store: dict[str, dict[str, Data]] = {}
        self.backupStore: dict[str, dict[str, Data]] = {}

    def makeQuery(self, query: list[str]) -> str:
        action = query[0]
        queryData = query[1:]
        if action == 'SET' or action == 'SET_AT' or action == 'SET_AT_WITH_TTL':
            return self._set(*queryData)
        elif action == 'GET' or action == 'GET_AT':
            return self._get(*queryData)
        elif action == 'DELETE' or action == 'DELETE_AT':
            return self._delete(*queryData)
        elif action == 'SCAN' or action == 'SCAN_AT':
            return self._scan(*queryData)
        elif action == 'SCAN_BY_PREFIX' or action == 'SCAN_BY_PREFIX_AT':
            return self._scanByPrefix(*queryData)
        elif action == 'BACKUP_KEY':
            return self._backup_key(*queryData)
        elif action == 'RESTORE_KEY':
            return self._restore_key(*queryData)
        elif action == 'BACKUP':
            return self._backup(*queryData)
        elif action == 'RESTORE':
            return self._restore(*queryData)
        return ''
    
    def _set(self, namespace: str, key: str, value: str, ts: str = '', ttl: str = '') -> str:
        table = self.store.setdefault(namespace, {})
        table[key] = Data(value, ts, ttl)
        return ''
    
    def _get(self, namespace: str, key: str, ts: str = '') -> str:
        table = self.store.get(namespace)
        if table == None: return ''
        data = table.get(key, self.emptyData)
        if not data.isActive(ts):
            del table[key]
            return ''
        return data.value
        
    def _delete(self, namespace: str, key: str, ts: str = '') -> str:
        table = self.store.get(namespace)
        if table == None: return self.FAILED
        data = table.get(key)
        if data == None: return self.FAILED
        del table[key]
        if not data.isActive(ts):
            return self.FAILED
        return self.OK
    
    def _scan(self, namespace: str, ts: str = '') -> str:
        return self._scanByPrefix(namespace, ts)
    
    def _scanByPrefix(self, namespace: str, prefix: str = '', ts: str = '') -> str:
        table = self.store.get(namespace)
        if table == None: return ''
        strItems = [f'{k}({data.value})' for k, data in table.items() if k.startswith(prefix) and data.isActive(ts)]
        return ', '.join(strItems)

    def _move(self, namespace: str, key: str, fromStore: dict[str, dict[str, Data]], toStore: dict[str, dict[str, Data]]) -> str:
        fromTable = fromStore.get(namespace)
        if fromTable == None: return self.FAILED
        if key not in fromTable: return self.FAILED
        toTable = toStore.setdefault(namespace, {})
        toTable[key] = fromTable[key]
        del fromTable[key]
        return self.OK
    
    def _backup_key(self, namespace: str, key: str) -> str:
        return self._move(namespace, key, self.store, self.backupStore)
    
    def _restore_key(self, namespace: str, key: str) -> str:
        return self._move(namespace, key, self.backupStore, self.store)
    
    def _backup(self, path: str) -> str:
        try:
            with open(path, 'wb') as file:
                pickle.dump(self.store, file)
        except:
            return self.FAILED
        self.store = {}
        return self.OK
    
    def _restore(self, path: str) -> str:
        try:
            with open(path, 'rb') as file:
                self.store = pickle.load(file)
            return self.OK
        except:
            return self.FAILED
        

def test_no_timestamp_cases():
    kvStore = KVStore()
    assert kvStore.makeQuery(["SET", "NAMESPACE_1", "KEY_1", "VALUE_1", ""]) == ''
    assert kvStore.makeQuery(["SET", "NAMESPACE_1", "KEY_2", "VALUE_2"]) == ''
    assert kvStore.makeQuery(["SET", "NAMESPACE_2", "KEY_3", "VALUE_3"]) == ''

    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_1"]) == 'VALUE_1'
    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_2"]) == 'VALUE_2'
    assert kvStore.makeQuery(["GET", "NAMESPACE_2", "KEY_1"]) == ''

    assert kvStore.makeQuery(["SET", "NAMESPACE_1", "KEY_1", "VALUE_1_a"]) == ''
    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_1"]) == 'VALUE_1_a'

    assert kvStore.makeQuery(["DELETE", "NAMESPACE_1", "KEY_2"]) == 'true'
    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_2"]) == ''

    assert kvStore.makeQuery(["SCAN", "NAMESPACE_3"]) == ''
    assert kvStore.makeQuery(["SET", "NAMESPACE_1", "KEY_2", "VALUE_2"]) == ''
    assert kvStore.makeQuery(["SCAN", "NAMESPACE_1"]) == 'KEY_1(VALUE_1_a), KEY_2(VALUE_2)'
    assert kvStore.makeQuery(["SET", "NAMESPACE_1", "KEY_12", "VALUE_12"]) == ''
    assert kvStore.makeQuery(["SCAN_BY_PREFIX", "NAMESPACE_1", "KEY_NO"]) == ''
    assert kvStore.makeQuery(["SCAN_BY_PREFIX", "NAMESPACE_1", "KEY_1"]) == 'KEY_1(VALUE_1_a), KEY_12(VALUE_12)'

    assert kvStore.makeQuery(["BACKUP", "./test_data"]) == 'true'
    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_1"]) == ''
    assert kvStore.makeQuery(["SCAN_BY_PREFIX", "NAMESPACE_1", "KEY_1"]) == ''

    assert kvStore.makeQuery(["RESTORE", "./test_data"]) == 'true'
    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_1"]) == 'VALUE_1_a'
    assert kvStore.makeQuery(["SCAN_BY_PREFIX", "NAMESPACE_1", "KEY_1"]) == 'KEY_1(VALUE_1_a), KEY_12(VALUE_12)'

def test_timestamp_cases():
    kvStore = KVStore()
    assert kvStore.makeQuery(["SET", "NAMESPACE_1", "KEY_1", "VALUE_1", "1", "5"]) == ''
    assert kvStore.makeQuery(["SET", "NAMESPACE_1", "KEY_2", "VALUE_2", "2", "1"]) == ''
    assert kvStore.makeQuery(["SET", "NAMESPACE_2", "KEY_3", "VALUE_3", "2", "5"]) == ''

    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_1", "1"]) == 'VALUE_1'
    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_2", "2"]) == 'VALUE_2'
    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_2", "3"]) == ''
    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_1", "5"]) == 'VALUE_1'
    assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_1", "6"]) == ''
    assert kvStore.makeQuery(["GET", "NAMESPACE_2", "KEY_1", "6"]) == ''
    assert kvStore.makeQuery(["GET", "NAMESPACE_2", "KEY_3", "6"]) == 'VALUE_3'

    assert kvStore.makeQuery(["SET", "NAMESPACE_2", "KEY_3", "VALUE_3_a", "6", "5"]) == ''
    assert kvStore.makeQuery(["GET", "NAMESPACE_2", "KEY_3", "10"]) == 'VALUE_3_a'
    assert kvStore.makeQuery(["GET", "NAMESPACE_2", "KEY_3", "11"]) == ''

    # assert kvStore.makeQuery(["DELETE", "NAMESPACE_1", "KEY_2"]) == 'true'
    # assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_2"]) == ''

    # assert kvStore.makeQuery(["SCAN", "NAMESPACE_3"]) == ''
    # assert kvStore.makeQuery(["SET", "NAMESPACE_1", "KEY_2", "VALUE_2"]) == ''
    # assert kvStore.makeQuery(["SCAN", "NAMESPACE_1"]) == 'KEY_1(VALUE_1_a), KEY_2(VALUE_2)'
    # assert kvStore.makeQuery(["SET", "NAMESPACE_1", "KEY_12", "VALUE_12"]) == ''
    # assert kvStore.makeQuery(["SCAN_BY_PREFIX", "NAMESPACE_1", "KEY_NO"]) == ''
    # assert kvStore.makeQuery(["SCAN_BY_PREFIX", "NAMESPACE_1", "KEY_1"]) == 'KEY_1(VALUE_1_a), KEY_12(VALUE_12)'

    # assert kvStore.makeQuery(["BACKUP", "./kv_data"]) == 'true'
    # assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_1"]) == ''
    # assert kvStore.makeQuery(["SCAN_BY_PREFIX", "NAMESPACE_1", "KEY_1"]) == ''

    # assert kvStore.makeQuery(["RESTORE", "./kv_data"]) == 'true'
    # assert kvStore.makeQuery(["GET", "NAMESPACE_1", "KEY_1"]) == 'VALUE_1_a'
    # assert kvStore.makeQuery(["SCAN_BY_PREFIX", "NAMESPACE_1", "KEY_1"]) == 'KEY_1(VALUE_1_a), KEY_12(VALUE_12)'

if __name__ == '__main__':
    # test_no_timestamp_cases()
    test_timestamp_cases()


    
    