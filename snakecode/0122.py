class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pre, maxProfit = prices[0], 0
        for cur in prices:
            maxProfit += max(cur-pre, 0)
            pre = cur
        return maxProfit