from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, curMin = 0, prices[0]
        for p in prices:
            if p >= curMin:
                res = max(res, p - curMin)
            else:
                curMin = p
        return res