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