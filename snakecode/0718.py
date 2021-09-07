class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        dp: list[list[int]] = [[0 for _ in nums2] for _ in nums1]
        maxLen: int = 0
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                    maxLen = max(dp[i][j], maxLen)
        return maxLen

    def findLength2(self, nums1: list[int], nums2: list[int]) -> int:
        dp: list[int] = [0 for _ in range(len(nums2)+1)]
        maxLen: int = 0
        for i in range(len(nums1)):
            for j in range(len(nums2), 0, -1):
                if nums1[i] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                    maxLen = max(dp[j], maxLen)
                else:
                    dp[j] = 0
        return maxLen
