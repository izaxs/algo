# Number of Enclaves

# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 500
#     grid[i][j] is either 0 or 1.

class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def search(x: int, y: int) -> int:
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])): return -1
            if grid[x][y] == 0: return 0
            grid[x][y], enclaves, off = 0, 1, False
            for dx, dy in DIRS:
                if (e := search(x+dx, y+dy)) >= 0: enclaves += e
                else: off = True # Don't return because search has not finished yet! This bug is hard to figure out
            return enclaves if not off else -1
        count = 0
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell == 1 and (e := search(x, y)) >= 0:
                    count += e
        return count
    
    def numEnclaves2(self, grid: list[list[int]]) -> int:
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfsCancel(x: int, y: int):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or not grid[x][y]: return
            grid[x][y] = 0
            for dx, dy in DIRS:
                dfsCancel(x+dx, y+dy)
        if len(grid) <= 2 or len(grid[0]) <= 2: return 0
        for i in range(len(grid)):
            dfsCancel(i, 0)
            dfsCancel(i, len(grid[0])-1)
        for i in range(len(grid[0])):
            dfsCancel(0, i)
            dfsCancel(len(grid)-1, i)
        return sum(sum(i) for i in grid)

if __name__ == '__main__':
    matrix1 = [
        [0,0,0,0],
        [1,0,1,0],
        [0,1,1,0],
        [0,0,0,0],
    ]
    matrix2 = [
        [0,0,1,1,1,0,1,1,1,0,1],
        [1,1,1,1,0,1,0,1,1,0,0],
        [0,1,0,1,1,0,0,0,0,1,0],
        [1,0,1,1,1,1,1,0,0,0,1],
        [0,0,1,0,1,1,0,0,1,0,0],
        [1,0,0,1,1,1,0,0,0,1,1],
        [0,1,0,1,1,0,0,0,1,0,0],
        [0,1,1,0,1,0,1,1,1,0,0],
        [1,1,0,1,1,1,0,0,0,0,0],
        [1,0,1,1,0,0,0,1,0,0,1],
    ]
    c = Solution().numEnclaves2(matrix1)
    print(c)