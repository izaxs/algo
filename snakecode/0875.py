class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo, hi = 0, max(piles)+1
        while lo < hi:
            mid: int = (lo+hi)//2
            needTime = self.time(piles, mid)
            if needTime <= h:
                hi = mid
            else:
                lo = mid+1
        return lo

    def time(self, piles: list[int], k: int) -> int:
        res = 0
        for i in piles:
            res += i//k + int(i % k != 0)
        return res