# Min Cost Climbing Stairs

# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Constraints:

#     2 <= cost.length <= 1000
#     0 <= cost[i] <= 999


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n0, n1 = (0, 0), (1, 0) # (index, cost)
        for _ in range(len(cost)-1):
            n0, n1 = n1, (n1[0]+1, min(cost[n0[0]]+n0[1], cost[n1[0]]+n1[1]))
        return n1[1]

    def minCostClimbingStairs2(self, cost: list[int]) -> int:
        n0, n1 = 0, 0
        for i in range(1, len(cost)):
            n0, n1 = n1, min(cost[i-1]+n0, cost[i]+n1)
        return n1

if __name__ == "__main__":
    cost = [10, 15, 20]
    print(Solution().minCostClimbingStairs2(cost))