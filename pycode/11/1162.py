# As Far from Land as Possible

# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

# Constraints:

#     n == grid.length
#     n == grid[i].length
#     1 <= n <= 100
#     grid[i][j] is 0 or 1

import math, include
import printer

class Solution:

    # BFS Time exceed, starting from water is inefficient
    def maxDistance(self, grid: list[list[int]]) -> int:
        def canGo(x: int, y: int) -> bool:
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] >= 0
        def getDistance(x: int, y: int) -> int:
            if (not canGo(x, y)) or grid[x][y] == 1: return -1
            visitOrder, level, visited = [(x, y)], 1, 0
            while visited < len(visitOrder):
                size = len(visitOrder)-visited
                for _ in range(size):
                    nx, ny = visitOrder[visited]
                    # print(f'{nx=} {ny=}')
                    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        xx, yy = nx+dx, ny+dy
                        if not canGo(xx, yy): continue
                        if grid[xx][yy] == 1:
                            # printer.print2D(grid)
                            for nx, ny in visitOrder:
                                grid[nx][ny] = 0
                            # print(f"{x=} {y=} {level=}")
                            return level
                        visitOrder.append((nx+dx, ny+dy))
                        grid[nx+dx][ny+dy] = -1
                    visited += 1
                level += 1
            return -1

        maxDis = -1
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                maxDis = max(maxDis, getDistance(i, j))
        return maxDis

    # BFS, start from islands
    def maxDistance2(self, grid: list[list[int]]) -> int:
        visitOrder = [(x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == 1]
        if len(visitOrder) == len(grid)*len(grid[0]): return -1
        dryLevel, visited = -1, 0
        while visited < len(visitOrder):
            dryLevel += 1
            size = len(visitOrder)-visited
            for _ in range(size):
                x, y = visitOrder[visited]
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xx, yy = x+dx, y+dy
                    if xx < 0 or xx >= len(grid) or yy < 0 or yy >= len(grid[0]) or grid[xx][yy] == 1: continue
                    visitOrder.append((xx, yy))
                    grid[xx][yy] = 1
                visited += 1
        return dryLevel
        
if __name__ == "__main__":
    grid0 = [
        [1,0,1],
        [0,0,0],
        [1,0,1],
    ]
    grid1 = [
        [1,0,0],
        [0,0,0],
        [0,0,0],
    ]
    assert Solution().maxDistance2(grid0) == 2
    assert Solution().maxDistance2(grid1) == 4
            
        