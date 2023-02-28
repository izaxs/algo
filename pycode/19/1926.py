# Nearest Exit from Entrance in Maze

# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

# Constraints:

# maze.length == m
# maze[i].length == n
# 1 <= m, n <= 100
# maze[i][j] is either '.' or '+'.
# entrance.length == 2
# 0 <= entrancerow < m
# 0 <= entrancecol < n
# entrance will always be an empty cell.
from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        PATH, WALL, VISITED, M, N = '.', '+', '*', len(maze), len(maze[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def isExit(x: int, y: int) -> bool:
            return maze[x][y] == PATH and (x == 0 or x == M-1 or y == 0 or y == N-1)
        def canMove(x: int, y: int) -> bool:
            return 0 <= x < M and 0 <= y < N and maze[x][y] == PATH
        dq: deque[tuple[int, int]] = deque()
        x, y = entrance
        maze[x][y], steps = VISITED, 1
        dq.append((x, y))
        while dq:
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                for dx, dy in DIRS:
                    xx, yy = x+dx, y+dy
                    if not canMove(xx, yy): continue
                    if isExit(xx, yy): return steps
                    maze[xx][yy] = VISITED
                    dq.append((xx, yy))
            steps += 1
        return -1
