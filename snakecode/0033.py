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