def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    i, longest, tail = -1, 0, -1
    for i, v in enumerate(s):
        if v in seen:
            tail = max(tail, seen[v])
        seen[v] = i
        longest = max(longest, i - tail)
    return longest


print(lengthOfLongestSubstring("abba"))
print(lengthOfLongestSubstring("abacdefcd"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))