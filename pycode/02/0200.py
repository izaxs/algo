# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 300
#     grid[i][j] is '0' or '1'.


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def numIslands(self, grid: list[list[str]]) -> int:
        self.grid = grid
        self.xLen, self.yLen = len(grid), len(grid[0])
        self.marked = [[False] * len(line) for line in grid]
        counter = 0
        for x, line in enumerate(grid):
            for y, _ in enumerate(line):
                land = self.search(x, y)
                counter += land
        return counter

    def search(self, x: int, y: int) -> int:
        if x < 0 or x >= self.xLen or y < 0 or y >= self.yLen or self.marked[x][y]:
            return 0
        self.marked[x][y] = True
        if self.grid[x][y] == '0':
            return 0
        for xx, yy in self.DIRS:
            self.search(x + xx, y + yy)
        return 1

    def numIslands2(self, grid: list[list[str]]) -> int:
        def dfs(x: int, y: int):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1'):
                return
            grid[x][y] = '0'
            for dx, dy in self.DIRS:
                dfs(x+dx, y+dy)
        count = 0
        for x, row in enumerate(grid):
            for y, v in enumerate(row):
                if v == '1':
                    count += 1
                    dfs(x, y)
        return count
    
    def numIslands3(self, grid: list[list[str]]) -> int:
        DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        m, n = len(grid), len(grid[0])
        def search(x: int, y: int):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] == '1'): return
            grid[x][y] = ''
            for dx, dy in DIRS:
                search(x+dx, y+dy)
        counter = 0
        for x, row in enumerate(grid):
            for y, v in enumerate(row):
                if v == '1':
                    counter += 1
                    search(x, y)
        return counter
            

if __name__ == '__main__':
    s = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    n = s.numIslands(grid)
    print(n)