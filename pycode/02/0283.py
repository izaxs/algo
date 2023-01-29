# Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        cur = 0
        for n in nums:
            if n:
                nums[cur] = n
                cur += 1
        for i in range(cur, len(nums)):
            nums[i] = 0

    def moveZeroes2(self, nums: list[int]) -> None:
        cur = 0
        for i, n in enumerate(nums):
            if n:
                nums[cur] = n
                nums[i] = 0 if cur != i else n
                cur += 1
        