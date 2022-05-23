import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        closest = heapq.nsmallest(k, points, lambda x: x[0] ** 2 + x[1] ** 2)
        return closest

    # Quick select with partition sort
    def kClosest2(self, points: list[list[int]], k: int) -> list[list[int]]:
        if k >= len(points): return points

        def dist(point: list[int]) -> int:
            return point[0]**2+point[1]**2

        def partition(points: list[list[int]], lo: int, hi: int) -> int:
            pivot, insert = dist(points[hi]), lo
            for i in range(lo, hi):
                if dist(points[i]) < pivot:
                    points[insert], points[i] = points[i], points[insert]
                    insert += 1
            points[insert], points[hi] = points[hi], points[insert]
            return insert

        lo, hi = 0, len(points)-1
        while lo < hi:
            mid = partition(points, lo, hi)
            if mid < k-1:
                lo = mid+1
            elif mid > k-1:
                hi = mid-1
            else:
                return points[:mid+1]
        return points[:lo+1]
