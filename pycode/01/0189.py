# Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Constraints:

    # 1 <= nums.length <= 105
    # -231 <= nums[i] <= 231 - 1
    # 0 <= k <= 105

# Follow up:

#     Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
#     Could you do it in-place with O(1) extra space?
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        def reverse(lo = 0, hi = len(nums)-1):
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo, hi = lo+1, hi-1
        offset = len(nums) - (k % len(nums))
        reverse(hi = offset-1)
        reverse(lo = offset)
        reverse()