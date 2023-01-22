# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import random

# Dummy function for conveniency
def isBadVersion(version: int) -> bool:
    return random.randrange(0, 10) == version % 10

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n+1
        while lo < hi:
            mid = (lo+hi) >> 1
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                hi = mid
            else:
                lo = mid+1
        return lo
