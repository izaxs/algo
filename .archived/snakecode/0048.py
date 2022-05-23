class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        self.diagMirror(matrix)
        self.verticalMirror(matrix)

    def diagMirror(self, matrix: list[list[int]]):
        width = len(matrix)
        for x in range(width):
            for y in range(x, width):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    def verticalMirror(self, matrix: list[list[int]]):
        width = len(matrix)
        for x in range(width):
            for y in range(width//2):
                matrix[x][y], matrix[x][width-1-y] = matrix[x][width-1-y], matrix[x][y]
