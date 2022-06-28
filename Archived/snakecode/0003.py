class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, tail = 0, -1
        seen: dict[str, int] = {}
        for i, v in enumerate(s):
            tail = max(tail, seen.get(v, -1))
            res = max(res, i - tail)
            seen[v] = i
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abba"))
    print(s.lengthOfLongestSubstring("abacdefcd"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(""))
