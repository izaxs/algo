# Pacific Atlantic Water Flow

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Constraints:

#     m == heights.length
#     n == heights[r].length
#     1 <= m, n <= 200
#     0 <= heights[r][c] <= 105
import include
from collections import deque
from printer import print2d

class Solution:
    # BFS from sea
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # cell mask 1 for Pacific, mask 2 for Atlantic
        flood = [[0]*len(heights[0]) for _ in heights]
        Q: deque[tuple[int, int]] = deque()

        def canFlow(x: int, y: int, xx: int, yy: int, floodType: int) -> bool:
            if not (0 <= xx < len(flood) and 0 <= yy < len(flood[0])): return False
            # Don't forget to check with &floodType!
            return flood[xx][yy]&floodType == 0 and heights[x][y] <= heights[xx][yy] 

        def makeFlood(floodType: int):
            while Q:
                size = len(Q)
                for _ in range(size):
                    x, y = Q.popleft()
                    flood[x][y] |= floodType
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        xx, yy = x+dx, y+dy
                        if canFlow(x, y, xx, yy, floodType): Q.append((xx, yy))
        
        for i in range(len(heights)): Q.append((i, 0))
        for i in range(len(heights[0])): Q.append((0, i))
        makeFlood(1)
        for i in range(len(heights)): Q.append((i, len(heights[0])-1))
        for i in range(len(heights[0])): Q.append((len(heights)-1, i))
        makeFlood(2)
        return [[i, j] for i, row in enumerate(flood) for j, cell in enumerate(row) if cell == 3]

    # DFS from sea, faster
    def pacificAtlantic2(self, heights: list[list[int]]) -> list[list[int]]:
        # cell mask 1 for Pacific, mask 2 for Atlantic
        flood = [[0]*len(heights[0]) for _ in heights]
        def dfs(x: int, y: int, xx: int, yy: int, floodType: int):
            if not (0 <= xx < len(heights) and 0 <= yy < len(heights[0])): return
            if x == -1 or (flood[xx][yy]&floodType == 0 and heights[x][y] <= heights[xx][yy]):
                flood[xx][yy] |= floodType
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dfs(xx, yy, xx+dx, yy+dy, floodType)
        for i in range(len(heights)): 
            dfs(-1, -1, i, 0, 1)
            dfs(-1, -1, i, len(heights[0])-1, 2)
        for j in range(len(heights[0])):
            dfs(-1, -1, 0, j, 1)
            dfs(-1, -1, len(heights)-1, j, 2)
        return [[i, j] for i, row in enumerate(flood) for j, cell in enumerate(row) if cell == 3]

if __name__ == "__main__":
    H = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]]
    F = Solution().pacificAtlantic(H)

        