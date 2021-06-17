class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        table: dict[tuple[str, ...], list[str]] = {}
        for s in strs:
            ss = tuple(sorted(s))
            table.setdefault(ss, []).append(s)
        return list(table.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
