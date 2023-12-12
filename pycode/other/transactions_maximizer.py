# Maximize transaction profits
# With transaction size and dependencies as the constrains

def maxProfit(sizes: list[int], profits: list[int], deps: list[int], maxCap: int) -> int:
    def getTreeValues(nth: int, fromVals: list[int], toVals: list[int]) -> int:
        if toVals[nth] != -1: return toVals[nth]
        toVals[nth] = fromVals[nth]
        if deps[nth] != -1:
            toVals[nth] += getTreeValues(deps[nth], fromVals, toVals)
        return toVals[nth]
            
    def getProfit(curCap: int, nth: int) -> int:
        if curCap <= 0 or nth == 0: return 0
        if dp[curCap][nth] != -1:
            pass
        elif realSizes[nth-1] > curCap:
            dp[curCap][nth] = getProfit(curCap, nth-1)
        else:
            dp[curCap][nth] = max(
                getProfit(curCap, nth-1),
                realProfits[nth - 1] + getProfit(curCap - realSizes[nth-1], nth-1)
            )
        return dp[curCap][nth]
        


    N = len(sizes)
    realSizes = [-1 for _ in range(N)]
    realProfits = [-1 for _ in range(N)]
    for i in range(N): 
        getTreeValues(i, sizes, realSizes)
        getTreeValues(i, profits, realProfits)
    dp = [[-1 for _ in range(N + 1)] for _ in range(maxCap + 1)]
    dp[0][0] = 0
    
    return getProfit(maxCap, N)

if __name__ == "__main__":
    profits = [60, 100, 150]
    sizes = [20, 30, 31]
    deps = [-1, -1, 1]
    capacity = 65
    n = len(profits)
    result = maxProfit(sizes, profits, deps, capacity)

    print(result)
