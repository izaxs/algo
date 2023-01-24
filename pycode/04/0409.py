# Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter: list[int] = [0]*64
        base = ord('A')
        for c in s:
            counter[ord(c)-base] += 1
        withSingle = 0
        length = 0
        for i in counter:
            length += i >> 1
            withSingle |= i
        return (length<<1)+(withSingle&1)

    def longestPalindrome2(self, s: str) -> int:
        counter: list[int] = [0]*64
        base, odds = ord('A'), 0
        for c in s:
            counter[ord(c)-base] += 1
        for i in counter:
            odds += i&1
        return len(s)-odds+int(odds>0)
