class Transaction:
    def __init__(self, msg: str) -> None:
        parsed = msg.split(',')
        self.name: str = parsed[0]
        self.time: int = int(parsed[1])
        self.cost: int = int(parsed[2])
        self.city: str = parsed[3]

    def __str__(self) -> str:
        return ','.join((self.name, str(self.time), str(self.cost), self.city))

# This implementation is wrong, not fully understand the question, all related invalid transactions should be taken into account
class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        wait = 60
        trans = [Transaction(i) for i in transactions]
        trans.sort(key=lambda x: x.time)
        invalid: list[Transaction] = []
        watcher: dict[str, tuple[str, int]] = {}
        for t in trans:
            if t.cost > 1000:
                invalid.append(t)
                continue
            if t.name in watcher:
                city, until = watcher[t.name]
                if t.city != city and t.time < until:
                    invalid.append(t)
                    continue
            watcher[t.name] = (t.city, t.time+wait)
        return [str(t) for t in invalid]
