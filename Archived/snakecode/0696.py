class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res: int = 0
        pre: int = 0
        cur: int = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                res += min(pre, cur)
                pre = cur
                cur = 1
        res += min(pre, cur)
        return res