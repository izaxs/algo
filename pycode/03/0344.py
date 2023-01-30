# Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: list[str]) -> None:
        lo, hi = 0, len(s)-1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo, hi = lo+1, hi-1