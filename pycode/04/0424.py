# Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = [0]*26
        start = maxLen = maxFreq = 0
        for end, ch in enumerate(s):
            charOrd = ord(ch)-ord('A')
            freqs[charOrd] += 1
            maxFreq = max(maxFreq, freqs[charOrd])
            if end-start+1-maxFreq > k:
                freqs[ord(s[start])-ord('A')] -= 1
                start += 1
            maxLen = max(maxLen, end-start+1)
        return maxLen

if __name__ == '__main__':
    Solution().characterReplacement("AABABBA", 1)
