class Solution:
    def validPalindrome(self, s: str) -> bool:
        # return self.helper(s, 0, len(s)-1, 1)
        return self.helper2(s, 0, len(s)-1, 1)

    def helper(self, s: str, lo: int, hi: int, k: int) -> bool:
        if lo >= hi:
            return True
        if s[lo] != s[hi]:
            if k > 0:
                return self.helper(s, lo+1, hi, k-1) or\
                    self.helper(s, lo, hi-1, k-1)
            else:
                return False
        return self.helper(s, lo+1, hi-1, k)

    def helper2(self, s: str, lo: int, hi: int, k: int) -> bool:
        while lo < hi:
            if s[lo] == s[hi]:
                lo += 1
                hi -= 1
            elif k > 0:
                return self.helper2(s, lo+1, hi, k-1) or\
                    self.helper2(s, lo, hi-1, k-1)
            else:
                return False
        return True

s = Solution()
print(s.validPalindrome("abca"))