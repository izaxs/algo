# Number of Closed Islands
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

# Constraints:

#     1 <= grid.length, grid[0].length <= 100
#     0 <= grid[i][j] <=1

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def reachedEdge(x: int, y: int) -> bool:
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                return True
            if grid[x][y] > 0:
                return False
            canReachEdge, grid[x][y] = False, 2
            for dx, dy in DIRS:
                canReachEdge |= reachedEdge(x+dx, y+dy)
            return canReachEdge
        count = 0
        for x, row in enumerate(grid):
            for y, v in enumerate(row):
                if v == 0:
                    count = count+1 if not reachedEdge(x, y) else count
        return count
        
