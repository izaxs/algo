from random import randrange

class Solution:

    def __init__(self, n: int, blacklist: list[int]):
        self.map: dict[int, int] = {}
        blocked = set(blacklist)
        end = n-len(blacklist)
        i = n-1
        for num in blacklist:
            if num >= end: continue
            while i in blocked: i -= 1
            self.map[num] = i
            i -= 1
        self.end = end

    def pick(self) -> int:
        num = randrange(0, self.end)
        num = self.map.get(num, num)
        return num

# Your Solution object will be instantiated and called as such:
obj = Solution(3, [0])
param_1 = obj.pick()