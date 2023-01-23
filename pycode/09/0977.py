# Given an integer array nums sorted in non-decreasing order
# Return an array of the squares of each number sorted in non-decreasing order.
from bisect import bisect_left

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        if not nums:
            return nums
        right = bisect_left(nums, 0)
        left = right-1
        nums = [i**2 for i in nums]
        res = [0]*len(nums)
        insert = 0
        while left >= 0 and right < len(nums):
            if nums[left] <= nums[right]:
                res[insert] = nums[left]
                left -= 1
            else:
                res[insert] = nums[right]
                right += 1
            insert += 1
        if left < 0:
            res[insert:] = nums[right:]
        else:
            res[insert:] = nums[left::-1]
        return res

    # No need to bisect at all ...
    def sortedSquares2(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums)-1
        nums = [i**2 for i in nums]
        res = [0]*len(nums)
        for i in range(len(res)-1, -1, -1):
            if nums[left] <= nums[right]:
                res[i] = nums[right]
                right -= 1
            else:
                res[i] = nums[left]
                left += 1
        return res

    # Improve space
    def sortedSquares3(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums)-1
        res = [0]*len(nums)
        for i in range(len(res)-1, -1, -1):
            leftV, rightV = abs(nums[left]), abs(nums[right])
            if leftV <= rightV:
                res[i] = rightV
                right -= 1
            else:
                res[i] = leftV
                left += 1
        for i in range(len(res)):
            res[i] = res[i]**2
        return res
