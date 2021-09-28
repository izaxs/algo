class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def take(day: int) -> int:
            count = 0
            cur = 0
            for d in bloomDay:
                if d > day:
                    cur = 0
                    continue
                cur += 1
                if cur == k:
                    count += 1
                    cur = 0
            return count
        maxDay = max(bloomDay)
        lo, hi = 0, maxDay+1
        while lo < hi:
            mid = (lo+hi) // 2
            count = take(mid)
            if count >= m:
                hi = mid
            else:
                lo = mid+1
        return lo if lo <= maxDay else -1
