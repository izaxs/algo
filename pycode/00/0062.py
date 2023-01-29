# Unique Paths

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Constraints:

#     1 <= m, n <= 100

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for _ in range(m-1):
            for i in range(1, n):
                dp[i] += dp[i-1]
        return dp[n-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        # C(m, n+m) = (n+m)!/(n!*m!)
        m, n = (n, m) if n < m else (m, n)
        mul, div, n = 1, 1, n-1
        for i in range(1, m):
            mul, div = mul*(n+i), div*i
        return mul//div

if __name__ == "__main__":
    print(Solution().uniquePaths2(1, 1))