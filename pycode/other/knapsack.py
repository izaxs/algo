# 01 Knapsack Problem

def solution():
    def knapsack(cap: int, nth: int) -> int:
        if cap <= 0 or nth == 0:
            return 0
        # print(f'{cap=} {nth=}')
        if thisProfit := dp[cap][nth] != -1: # result is already calculated
            return thisProfit
        if weights[nth-1] > cap: # if current nth item is larger than remaining capacity
            dp[cap][nth] = knapsack(cap, nth-1)
            return dp[cap][nth]
        dp[cap][nth] = max(
            values[nth-1] + knapsack(cap - weights[nth-1], nth-1), # with nth item
            knapsack(cap, nth-1)) # without nth item
        return dp[cap][nth]

    values = [60, 100, 150] 
    weights = [20, 30, 31] 
    capacity = 50
    n = len(values) 
      
    # Initialize the matrix with -1 at first.
    # dp[capacity][include_nth_item], dp[0][0] stands for 0 cap, no item
    dp = [[-1 for _ in range(n + 1)] for _ in range(capacity + 1)] 

    dp[0][0] = 0
    print(knapsack(capacity, n)) 


if __name__ == '__main__': 
    solution()