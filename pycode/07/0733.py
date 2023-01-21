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