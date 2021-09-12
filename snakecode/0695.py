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
