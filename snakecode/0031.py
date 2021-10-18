class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        def quickSort(lo: int, hi: int):
            if lo >= hi: return
            pivot, mid = nums[hi], lo
            for i in range(lo, hi):
                if nums[i] < pivot:
                    nums[mid], nums[i] = nums[i], nums[mid]
                    mid += 1
            nums[mid], nums[hi] = nums[hi], nums[mid]
            quickSort(lo, mid-1)
            quickSort(mid+1, hi)

        def search(lo: int, hi: int, largerThan: int):
            while lo < hi:
                mid = (lo+hi+1) >> 1
                if nums[mid] > largerThan: lo = mid
                else: hi = mid-1
            return hi

        target = len(nums)-1
        while target > 0 and nums[target-1] >= nums[target]: target -= 1
        if target > 0:
            swap1 = target-1
            swap2 = search(target, len(nums)-1, nums[swap1])
            nums[swap1], nums[swap2] = nums[swap2], nums[swap1]
        quickSort(target, len(nums)-1)

s = Solution()
nums = [1,3,2]
s.nextPermutation(nums)
print(nums)