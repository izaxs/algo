class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxItem, arraySum, maxSum = nums[0], 0, 0
        for i in nums:
            maxItem = max(maxItem, i)
            if i >= 0:
                arraySum += i
                maxSum = max(arraySum, maxSum)
            elif arraySum+i >= 0:
                arraySum += i
            else:
                arraySum = 0
        return maxSum if maxItem >= 0 else maxItem

    def maxSubArray2(self, nums: list[int]) -> int:
        arraySum = curMax = nums[0]
        for i in nums[1:]:
            arraySum = max(i, arraySum+i)
            curMax = max(arraySum, curMax)
        return curMax


s = Solution()
print(s.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))