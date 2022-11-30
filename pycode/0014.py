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
