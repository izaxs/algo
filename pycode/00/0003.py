# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.


# Constraints:

#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, tail = 0, -1
        seen: dict[str, int] = {}
        for i, v in enumerate(s):
            tail = max(tail, seen.get(v, -1))
            res = max(res, i - tail)
            seen[v] = i
        return res
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        longest, tail = 0, -1
        seen: dict[str, int] = {}
        for i, v in enumerate(s):
            tail = max(tail, seen.get(v, -1))
            longest = max(longest, i-tail)
            seen[v] = i
        return longest

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abba"))
    print(s.lengthOfLongestSubstring("abacdefcd"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(""))
