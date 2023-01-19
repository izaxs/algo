class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # e.g. nums: [1, 2, 3, 4] -> leftSum: [9, 7, 4, 0]
        leftSum = [0]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            leftSum[i] = nums[i+1]+leftSum[i+1]
        curSum = 0
        for i, v in enumerate(nums):
            if curSum == leftSum[i]:
                return i
            curSum += v
        return -1

    def pivotIndex2(self, nums: list[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i, v in enumerate(nums):
            if leftSum == total-leftSum-v:
                return i
            leftSum += v
        return -1
