class Solution:
    def find_min(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums)
        while lo < hi and nums[hi-1] == nums[0]: hi -= 1 # tricky
        if hi == 0: return -1
        while lo < hi:
            mid: int = (lo+hi) // 2
            if nums[mid] >= nums[0]: lo = mid+1
            else: hi = mid
        return lo

    def bi_search(self, nums: list[int], target: int, lo: int, hi: int) -> bool:
        while lo < hi:
            mid: int = (lo+hi) // 2
            if nums[mid] < target: lo = mid+1
            elif nums[mid] > target: hi = mid
            else: return True
        return False

    def search(self, nums: list[int], target: int) -> bool:
        if not nums: return False
        pivot = self.find_min(nums)
        if pivot == -1: return nums[0] == target
        if nums[0] <= target: return self.bi_search(nums, target, 0, pivot)
        return self.bi_search(nums, target, pivot, len(nums))
        