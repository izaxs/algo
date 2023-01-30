# Max Area of Island

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 50
#     grid[i][j] is either 0 or 1.


class Solution:
    dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = [[False]*len(row) for row in grid]
        maxArea = 0
        for x, row in enumerate(grid):
            for y, _ in enumerate(row):
                maxArea = max(maxArea, self.search(grid, visited, x, y))
        return maxArea

    def search(self, grid: list[list[int]], visited: list[list[bool]], x: int, y: int) -> int:
        if not (0 <= x <= len(grid)) or not (0 <= y <= len(grid[0])) or visited[x][y] or grid[x][y] == 0: return 0
        visited[x][y] = True
        area = grid[x][y]
        for dx, dy in Solution.dirs:
            area += self.search(grid, visited, x+dx, y+dy)
        return area

    def maxAreaOfIsland2(self, grid: list[list[int]]) -> int:
        rowL, colL = len(grid), len(grid[0])
        dirs = ((1,0), (0, 1), (-1, 0), (0, -1))

        def search(x: int, y: int) -> int:
            area = 0
            if (0 <= x < rowL) and (0 <= y < colL) and grid[x][y]:
                area += grid[x][y]
                grid[x][y] = 0
                for dx, dy in dirs:
                    area += search(x+dx, y+dy)
            return area
        maxArea = 0

        for x in range(rowL):
            for y in range(colL):
                maxArea = max(maxArea, search(x, y))
        return maxArea

class Solution2:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]
        def searchArea(x: int, y: int) -> int:
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1):
                return 0
            area, grid[x][y] = 1, 0
            for dx, dy in dirs:
                area += searchArea(x+dx, y+dy)
            return area
        maxArea = 0
        for x, row in enumerate(grid):
            for y, _ in enumerate(row):
                maxArea = max(maxArea, searchArea(x, y))
        return maxArea