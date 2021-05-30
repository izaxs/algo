from typing import List

class Solution:
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def numIslands(self, grid: List[List[str]]) -> int:
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
        for xx, yy in self.dirs:
            self.search(x + xx, y + yy)
        return 1

s = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
n = s.numIslands(grid)
print(n)