# Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Constraints:

#     1 <= nums.length <= 104
#     -104 <= nums[i] <= 104
#     nums contains distinct values sorted in ascending order.
#     -104 <= target <= 104

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo+((hi-lo)>>1)
            if nums[mid] < target:
                lo = mid+1
            elif nums[mid] > target:
                hi = mid
            else:
                return mid
        return lo