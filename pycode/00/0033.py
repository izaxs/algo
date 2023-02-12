# Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.
 
# Constraints:

#     1 <= nums.length <= 5000
#     -104 <= nums[i] <= 104
#     All values of nums are unique.
#     nums is an ascending array that is possibly rotated.
#     -104 <= target <= 104


class Solution:
    def find_min(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid: int = (lo+hi) // 2
            if nums[mid] >= nums[0]: lo = mid+1
            else: hi = mid
        return lo

    def bi_search(self, nums: list[int], target: int, lo: int, hi: int) -> int:
        while lo < hi:
            mid: int = (lo+hi) // 2
            if nums[mid] < target: lo = mid+1
            elif nums[mid] > target: hi = mid
            else: return mid
        return -1

    def search(self, nums: list[int], target: int) -> int:
        if not nums: return -1
        pivot = self.find_min(nums)
        if nums[0] <= target: return self.bi_search(nums, target, 0, pivot)
        return self.bi_search(nums, target, pivot, len(nums))