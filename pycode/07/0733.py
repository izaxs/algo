# Flood Fill
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# Constraints:

#     m == image.length
#     n == image[i].length
#     1 <= m, n <= 50
#     0 <= image[i][j], color < 216
#     0 <= sr < m
#     0 <= sc < n


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def canReach(r, c, preColor) -> bool:
            return 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == preColor

        def dfs(rr: int, cc: int):
            preColor = image[rr][cc]
            if preColor == color:
                return
            image[rr][cc] = color
            for dr, dc in dirs:
                r, c = rr+dr, cc+dc
                if canReach(r, c, preColor):
                    dfs(r, c)
        
        dfs(sr, sc)
        return image

    def floodFill2(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def canGo(x: int, y: int, preColor: int):
            return 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == preColor
        
        def mark(x: int, y: int):
            preColor = image[x][y]
            image[x][y] = color
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if canGo(nx, ny, preColor):
                    mark(nx, ny)

        if image[sr][sc] != color:
            mark(sr, sc)
        return image

if __name__ == "__main__":
    import include
    from printer import print2D
    s = Solution()
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    s.floodFill(image, 1, 1, 2)
    print2D(image)