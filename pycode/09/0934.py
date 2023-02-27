# Shortest Bridge

# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

# Constraints:

#     n == grid.length == grid[i].length
#     2 <= n <= 100
#     grid[i][j] is either 0 or 1.
#     There are exactly two islands in grid.
from collections import deque

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        N = len(grid)
        dq: deque[tuple[int, int]] = deque()
        def markIsland(x: int, y: int):
            if not (0 <= x < N and 0 <= y < N and grid[x][y] == 1): return
            grid[x][y] = 0
            dq.append((x, y))
            for dx, dy in DIRS:
                markIsland(x+dx, y+dy)
        def findAndMarkIsland():
            for i, row in enumerate(grid):
                for j, cell in enumerate(row):
                    if cell == 1:
                        markIsland(i, j)
                        return
        findAndMarkIsland()
        distance = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                if not (0 <= x < N and 0 <= y < N and grid[x][y] >= 0): continue
                if grid[x][y] == 1: return distance-1
                grid[x][y] = -1
                for dx, dy in DIRS:
                    dq.append((x+dx, y+dy))
            distance += 1
        return -1