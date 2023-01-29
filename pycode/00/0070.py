# Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Constraints:
# 1 <= n <= 45


class Solution:
    def climbStairs(self, n: int) -> int:
        n0, n1 = 1, 1 # 0th, 1st stairs
        for _ in range(n-1):
            n0, n1 = n1, n0+n1
        return n1