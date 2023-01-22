class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Considerably better because lo and hi both stop at the insertion point
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo+hi) >> 1
            if nums[mid] < target:
                lo = mid+1
            elif nums[mid] > target:
                hi = mid
            else:
                return mid
        return -1

    def search2(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi) >> 1
            if nums[mid] < target:
                lo = mid+1
            elif nums[mid] > target:
                lo = mid-1
            else:
                return mid
        return -1