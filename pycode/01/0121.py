# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res, curMin = 0, prices[0]
        for p in prices:
            if p >= curMin:
                res = max(res, p - curMin)
            else:
                curMin = p
        return res

    def maxProfit2(self, prices: list[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for p in prices:
            minPrice = min(minPrice, p)
            maxProfit = max(maxProfit, p-minPrice)
        return maxProfit
