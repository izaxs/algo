
# Implement Candy Crush.

# Candy Crush is a match-3 game where the player swaps candies on a grid, trying
# to make a row or column of 3 candies or more. When a swap results in a row or
# column of 3 or more candies, the candies in the row or column are crushed (removed
# from the board), and the empty spots are filled by having each column "fall down"
# and fill in the empty spaces. New random candies fall in from outside the grid to
# keep the grid full of candies. This process can trigger chain reactions. When a
# swap does not result in any crushing, the move is invalid and the candies are
# swapped back to their original positions.

# Here's an example: https://www.youtube.com/watch?v=jIlItUzW3Fg
# (Mute sound, skip to 0:05, and set playback to 0.25x)

# The task is the following: implement the main gameplay loop of Candy Crush. You
# will need to choose a representation for the game and implement a
# function (which can also be a method of a class, etc.)

# ```
# // This is pseudocode, not a real programming language.
# function swap(s state, p0 position, p1 position) boolean
# ```

# The function should return true if the move was a valid move that resulted in
# candies being crushed and the state of the game changing, and should return false
# if the move was invalid and resulted in no crushes, and therefore the state of the
# game did not change.

# You may assume that the state is stable at the beginning of any call to swap, i.e.
# before the swap is made there are no candies that can be crushed.

# Assume there are five kinds of candies, which can be identified by the colors red,
# green, blue, orange, and white.

from __future__ import annotations
from dataclasses import dataclass
from enum import IntEnum
import random

@dataclass
class Coordinate:
    x: int
    y: int

class Color(IntEnum):
    Empty = 0
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    ORANGE = 5

class Board(object):
    def __init__(self): # you fill in anything you want
        self.data: list[list[Candy]] = [[] for _ in range(7)]
        for row in self.data:
            for _ in range(7):
                row.append(random_candy())

    def crush(self) -> bool:
        D = self.data
        crushXY: set[tuple[int, int]] = set()
        # Mark
        for i in range(len(D)):
            for j in range(len(D[0])):
                if j > 1 and D[i][j] and D[i][j] == D[i][j-1] == D[i][j-2]:
                    crushXY |= {(i, j), (i, j-1), (i, j-2)}
                if i > 1 and D[i][j] and D[i][j] == D[i-1][j] == D[i-2][j]:
                    crushXY |= {(i, j), (i-1, j), (i-2, j)}

        if not crushXY: return False
        # print(f'will crush: {crushXY}')
        # Crush
        for i, j in crushXY: D[i][j] = Candy(Color.Empty)
        # print(f'crushed:\n{self}')
        return True

    def drop(self):
        D = self.data
        for j in range(len(D[0])):
            curRow = len(D)-1
            for i in range(len(D)-1, -1, -1):
                if D[i][j].color != Color.Empty:
                    D[curRow][j] = D[i][j]
                    curRow -= 1
            for i in range(curRow+1):
                D[i][j] = Candy(Color.Empty)

    def swap(self, coord1: Coordinate, coord2: Coordinate) -> bool:
        """
        If swapping the 2 results in "crushed" candies, then:
          a) Crush candies
          b) Apply gravity to have candies fall down.
          c) Fill candies from the top.
          d) Repeat a if any candies can be crushed.
          e) If no more candies can be crushed return True.
        If no candies would be "crushed" then swap the candies back
        and return False.
        """
        canCrush = False
        shouldContinue = True
        D = self.data
        D[coord1.x][coord1.y], D[coord2.x][coord2.y] = D[coord2.x][coord2.y], D[coord1.x][coord1.y]
        while shouldContinue:
            shouldContinue = self.crush()
            if shouldContinue: canCrush = True
            else: break
            self.drop()
        if not canCrush:
            D[coord1.x][coord1.y], D[coord2.x][coord2.y] = D[coord2.x][coord2.y], D[coord1.x][coord1.y]
            return False
        return True

    def __repr__(self) -> str:
        rowStrs: list[str] = []
        for row in self.data:
            rowStr = ''
            for candy in row:
                rowStr = rowStr + str(candy)
            rowStrs.append(rowStr)
        return '\n'.join(rowStrs)

class Candy(object):
    def __init__(self, color: Color):
        self.color = color

    def __bool__(self) -> bool:
        return self.color != Color.Empty

    def __repr__(self) -> str:
        return str(int(self.color))

    def __eq__(self, other: Candy) -> bool:
        return self.color == other.color

def random_candy():
    return Candy(random.choice(list(Color)))

# print(Candy(1) == Color.RED)
board = Board()
print(board, '\n')
while board.crush():
    board.drop()
print(board, '\n')
