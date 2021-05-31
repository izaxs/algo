import heapq

class Solution:    
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        closest = heapq.nsmallest(k, points, lambda x: x[0] ** 2 + x[1] ** 2)
        return closest


