# Last Stone Weight

# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

#     If x == y, both stones are destroyed, and
#     If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Constraints:

#     1 <= stones.length <= 30
#     1 <= stones[i] <= 1000
from heapq import heapify, heappop, heappush, heappushpop

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i, v in enumerate(stones):
            stones[i] = -v
        heapify(stones)
        pre = heappop(stones)
        while stones:
            cur = heappop(stones)
            if pre == cur:
                if stones:
                    pre = heappop(stones)
                else:
                    return 0
            else:
                pre = min(pre, cur) - max(pre, cur)
                pre = heappushpop(stones, pre)
        return -pre

    def lastStoneWeight2(self, stones: list[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1 and stones[0] != 0:
            heappush(stones, heappop(stones)-heappop(stones))
        return -stones[0]
        
if __name__ == '__main__':
    stones = [5, 4, 6, 2, 9, 0]
    Solution().lastStoneWeight2(stones)

        