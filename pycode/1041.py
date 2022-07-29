class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [complex(0, 1), complex(-1, 0), complex(0, -1), complex(1, 0)]
        dirIndex, coordinate = 0, complex(0, 0)
        for c in instructions:
            if c == 'R':
                dirIndex += 1
            elif c == 'L':
                dirIndex += 3
            else:
                coordinate += directions[dirIndex]
                continue
            dirIndex %= 4
        return coordinate == complex(0, 0) or dirIndex != 0

if __name__ == '__main__':
    s = Solution()
    dirs = "GGLLGG"
    print(s.isRobotBounded(dirs))
