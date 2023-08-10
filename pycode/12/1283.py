# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# The test cases are generated so that there will be an answer.
import math

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        # sum of the divisions range = [len(nums), sum(nums)]
        loBound, hiBound, maxNum = len(nums), sum(nums), max(nums)
        if threshold < loBound: raise ValueError("Threshold should be larger than length")
        if threshold == loBound: return maxNum
        if threshold >= hiBound: return 1
        lo, hi = 2, maxNum-1
        while lo < hi:
            mid = (lo+hi)//2
            curSum = sum(math.ceil(x/mid) for x in nums)
            if curSum <= threshold:
                hi = mid
            else:
                lo = mid+1
        return lo
    
if __name__ == "__main__":
    s = Solution()
    nums = [1,2,5,9]
    threshold = 6
    res = s.smallestDivisor(nums, threshold)
        
        