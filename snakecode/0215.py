from heapq import heapify


import heapq

class Solution:
    def findKthLargest1(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest2(self, nums: list[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

    def findKthLargest3(self, nums: list[int], k: int) -> int:
        pass