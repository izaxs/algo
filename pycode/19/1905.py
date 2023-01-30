# Count Sub Islands

# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

# Return the number of islands in grid2 that are considered sub-islands.

# Constraints:

#     m == grid1.length == grid2.length
#     n == grid1[i].length == grid2[i].length
#     1 <= m, n <= 500
#     grid1[i][j] and grid2[i][j] are either 0 or 1.

# Approach 1: 
# Give each island a group number in grid1
# For each island in grid2, if the cells mapped to grid1 has the same group number, consider the island as a sub island

# Approach 2:
# DFS cancel cells in grid2 that corresponding cell in grid1 is water
# Count the island in grid2

# Approach 3 (best):
# For every cell in grid2, DFS the island and make sure same cell in A is also a land cell
# No need to cancel anything because any mismatch between A, B means it's not sub island

class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            if not (0 <= x < len(grid2) and 0 <= y < len(grid2[0]) and grid2[x][y]): return 1
            isSub, grid2[x][y] = grid1[x][y], 0
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                isSub &= dfs(x+dx, y+dy)
            return isSub
        return sum(dfs(x, y) for x, row in enumerate(grid2) for y, cell in enumerate(row) if cell)
            
            