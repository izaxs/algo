# Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

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

    def expand(self, s: str, lo: int, hi: int) -> tuple[int, int]:
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo, hi = lo - 1, hi + 1
        return (lo + 1, hi - 1)  # return last valid indexes

    def longestPalindrome2(self, s: str) -> str:
        if len(s) <= 1: return s
        self.resLo, self.resHi = 0, 0
        for center in range(0, len(s)):
            for offset in [0, 1]:
                if self.shouldSkip(len(s), center, center+offset): continue
                curLo, curHi = self.expand2(s, center, center+offset)
                if curHi - curLo > self.resHi - self.resLo:
                    self.resLo, self.resHi = curLo, curHi
        return s[self.resLo:self.resHi+1]

    def expand2(self, s: str, lo: int, hi: int) -> tuple[int, int]:
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo, hi = lo-1, hi+1
        return (lo+1, hi-1)

    def shouldSkip(self, sLen: int, lo: int, hi: int) -> bool:
        maxHalf = min(lo, sLen-1-hi)
        maxLen = hi-lo+maxHalf*2+1
        return maxLen <= (self.resHi - self.resLo)
    
