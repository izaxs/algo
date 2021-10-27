# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

#     Insert a character
#     Delete a character
#     Replace a character


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2: return 0
        if not word1: return len(word2)
        if not word2: return len(word1)
        dp: list[list[int]] = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            dp[i][0] = i
        for j in range(1, len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[len(word1)][len(word2)]

    def minDistance2(self, word1: str, word2: str) -> int:
        if not word1 and not word2: return 0
        if not word1: return len(word2)
        if not word2: return len(word1)
        dp: list[int] = [0 for _ in range(len(word2)+1)]
        for j in range(1, len(word2)+1): dp[j] = j
        for i in range(1, len(word1)+1):
            lastReplaceCount = dp[0]
            dp[0] = i
            for j in range(1, len(word2)+1):
                curReplaceCount = dp[j]
                if word1[i-1] == word2[j-1]: dp[j] = lastReplaceCount
                else: dp[j] = 1+min(lastReplaceCount, dp[j-1], dp[j]) # on word1: replace, insert, delete
                lastReplaceCount = curReplaceCount
        return dp[len(word2)]
