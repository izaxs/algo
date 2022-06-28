from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counter = Counter(s)
        lower = 0
        for v in counter.values():
            if v & 1: lower += 1
        return lower <= k <= len(s)

    def canConstruct2(self, s: str, k: int) -> bool:
        if k > len(s): return False
        xor = 0
        offset = ord('a')
        for c in s:
            xor ^= 1 << (ord(c)-offset)
        while xor:
            k -= xor & 1
            if k < 0: return False
            xor >>= 1
        return True

s = Solution()
print(s.canConstruct2("cr", 7))