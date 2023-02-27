# 01 Matrix

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Constraints:

#     m == mat.length
#     n == mat[i].length
#     1 <= m, n <= 104
#     1 <= m * n <= 104
#     mat[i][j] is either 0 or 1.
#     There is at least one 0 in mat.
from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0]*n for _ in mat]
        distance = 0
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dq: deque[tuple[int, int]] = deque()
        dq.extend((i, j) for i, row in enumerate(mat) for j, cell in enumerate(row) if cell == 0)
        while dq:
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                if not (0 <= x < m and 0 <= y < n and mat[x][y] >= 0): continue
                mat[x][y] = -1
                res[x][y] = distance
                for dx, dy in DIRS:
                    dq.append((x+dx, y+dy))
            distance += 1
        return res