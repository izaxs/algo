# Next Permutation

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

#     For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

#     For example, the next permutation of arr = [1,2,3] is [1,3,2].
#     Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
#     While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

# Constraints:

#     1 <= nums.length <= 100
#     0 <= nums[i] <= 100


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # No need to sort, just reverse()
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

        def reverse(lo: int, hi: int):
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

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
        reverse(target, len(nums)-1)

s = Solution()
nums = [1,3,2]
s.nextPermutation(nums)
print(nums)