# Find All Anagrams in a String

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p): return []
        equator = [0]*26
        def diff() -> int: return sum(abs(i) for i in equator)
        for c in p: equator[ord(c)-ord('a')] -= 1
        for i in range(len(p)): equator[ord(s[i])-ord('a')] += 1
        res: list[int] = []
        if not (df := diff()): res.append(0)
        for i in range(len(s)-len(p)):
            equator[ord(s[i])-ord('a')] -= 1
            equator[ord(s[i+len(p)])-ord('a')] += 1
            # Can skip if at least 2 chars are different
            if df >= 4: df -= 2
            elif not (df := diff()): res.append(i+1)
        return res

if __name__ == '__main__':
    r = Solution().findAnagrams("cbaebabacd", "abc")
