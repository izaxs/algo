from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for s in strs:
            ss = tuple(sorted(s))
            table.setdefault(ss, []).append(s)
        return list(table.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))