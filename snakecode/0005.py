class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        limit, center, res = len(s) - 1, 0, (0, 0)
        while center < limit:
            cur = self.expand(s, center, center)
            if cur[1] - cur[0] > res[1] - res[0]:
                res = cur
            cur = self.expand(s, center, center + 1)
            if cur[1] - cur[0] > res[1] - res[0]:
                res = cur
            center += 1
        return s[res[0]:res[1] + 1]
    
    def expand(self, s: str, lo: int, hi: int) -> (int, int):
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo, hi = lo - 1, hi + 1
        return (lo + 1, hi - 1) # return last valid indexes