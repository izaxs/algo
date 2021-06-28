import heapq

class Solution:
    def findKthLargest1(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest2(self, nums: list[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

    def findKthLargest3(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for i in nums[k:]:
            heapq.heappushpop(heap, i)
        return heap[0]

    def findKthLargest(self, nums: list[int], k: int) -> int:
        return nums[self.find(nums, 0, len(nums)-1, k)]

    def find(self, nums: list[int], lo: int, hi: int, k: int) -> int:
        pivot = self.partition(nums, lo, hi)
        if pivot < k-1:
            return self.find(nums, pivot+1, hi, k)
        elif pivot > k-1:
            return self.find(nums, lo, pivot-1, k)
        else:
            return pivot

    def partition(self, nums: list[int], lo: int, hi: int) -> int:
        pivot: int = lo
        for i in range(lo, hi):
            if nums[i] > nums[hi]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1
        nums[pivot], nums[hi] = nums[hi], nums[pivot]
        return pivot

if __name__ == '__main__':
    s = Solution()
    # r = s.findKthLargest([3,2,1,5,6,4], 2)
    r = s.findKthLargest([1,1], 2)
    print(r)