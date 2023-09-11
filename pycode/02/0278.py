# 278. First Bad Version

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Constraints:

#     1 <= bad <= n <= 231 - 1

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
    
    def firstBadVersion2(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

