class TimeMap:

    def __init__(self):
        self.KV: dict[str, list[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        keychain = self.KV.setdefault(key, [])
        keychain.append((timestamp, value))
        # if key not in self.KV:
        #     self.KV[key] = [(timestamp, value)]
        # else:
        #     keychain = self.KV[key]
        #     isert: int = self.bisectRight(keychain, timestamp)
        #     keychain.append((timestamp, value))
        #     keychain[isert], keychain[-1] = keychain[-1], keychain[isert]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.KV:
            return ''
        keychain = self.KV[key]
        bound = self.bisectRight(keychain, timestamp)
        return keychain[bound-1][1] if bound > 0 else ''

    def bisectRight(self, vals: list[tuple[int, str]], timestamp: int) -> int:
        lo: int = 0
        hi: int = len(vals)

        while lo < hi:
            mid: int = (lo+hi)//2
            if vals[mid][0] <= timestamp:
                lo = mid+1
            else:
                hi = mid
        return lo

class TimeMap2:

    def __init__(self):
        self.KV: dict[str, list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        chain = self.KV.setdefault(key, [])
        chain.append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        chain = self.KV.get(key, [])
        if not chain: return ''
        lo = 0
        hi = len(chain)
        while lo < hi:
            mid: int = (lo+hi)//2
            if chain[mid][1] <= timestamp:
                lo = mid+1
            else:
                hi = mid
        if lo == 0:
            return ''
        return chain[lo-1][0]

if __name__ == '__main__':
    kv = TimeMap()
    kv.set('love', 'high', 10)
    kv.set('love', 'low', 20)
    v = kv.get('love', 5)
    print(v)