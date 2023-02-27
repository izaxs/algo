# Shortest Path in Binary Matrix

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

#     All the visited cells of the path are 0.
#     All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

# Constraints:

#     n == grid.length
#     n == grid[i].length
#     1 <= n <= 100
#     grid[i][j] is 0 or 1
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        def canReach(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < m and grid[x][y] == 0
        dirs = [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1)]
        m, res = len(grid), 1
        dq: deque[tuple[int, int]] = deque()
        dq.append((0, 0))
        while dq:
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                if not canReach(x, y): continue
                if x == m-1 and y == m-1: return res
                grid[x][y] = -1
                for dx, dy in dirs:
                    dq.append((x+dx, y+dy))
            res += 1
        return -1
