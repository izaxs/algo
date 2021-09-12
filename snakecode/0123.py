class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minVal = -1 << 34
        s1, s2, s3, s4 = -prices[0], minVal, minVal, minVal

        for i in range(1, len(prices)):
            s1 = max(s1, -prices[i])
            s2 = max(s2, s1+prices[i])
            s3 = max(s3, s2-prices[i])
            s4 = max(s4, s3+prices[i])
        return max(0, s4)