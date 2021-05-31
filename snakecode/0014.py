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
        
