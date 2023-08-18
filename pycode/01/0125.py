# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Constraints:

#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s)-1
        while lo < hi:
            loc, hic = s[lo],s[hi]
            if not loc.isalnum(): lo += 1
            elif not hic.isalnum(): hi -= 1
            elif loc.lower() != hic.lower(): 
                return False
            else:
                lo += 1
                hi -= 1
        return True
    
if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    Solution().isPalindrome(s)