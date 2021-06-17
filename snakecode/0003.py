def lengthOfLongestSubstring(s: str) -> int:
    res, tail = 0, -1
    seen: dict[str, int] = {}
    for i, v in enumerate(s):
        tail = max(tail, seen.get(v, -1))
        res = max(res, i - tail)
        seen[v] = i
    return res


print(lengthOfLongestSubstring("abba"))
print(lengthOfLongestSubstring("abacdefcd"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))
