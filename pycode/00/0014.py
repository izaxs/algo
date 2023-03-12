# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''
        base = min(strs, key=len)
        for i in range(len(base)):
            for s in strs:
                if base[i] != s[i]:
                    return base[:i]
        return base

    def longestCommonPrefix2(self, strs: list[str]) -> str:
        if not str: return ''
        effectiveBase = min(strs, key=len)
        for i in range(len(effectiveBase)):
            for s in strs:
                if s[i] != effectiveBase[i]:
                    return effectiveBase[:i]
        return effectiveBase

    def longestCommonPrefix3(self, strs: list[str]) -> str:
        baseStr = min(strs, key=len)
        for i, ch in enumerate(baseStr):
            for s in strs:
                if s[i] != ch:
                    return baseStr[:i]
        return baseStr

    def longestCommonPrefix4(self, strs: list[str]) -> str:
        s1, s2 = min(strs), max(strs)
        for i, ch in enumerate(s1):
            if ch != s2[i]: return s1[:i] # i is guaranteed to be in s2's range because of min(strs)
        return s1
