# 528. Random Pick with Weight

# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

# Constraints:

#     1 <= w.length <= 104
#     1 <= w[i] <= 105
#     pickIndex will be called at most 104 times.

from random import randrange

class Solution:

    def __init__(self, w: list[int]):
        self.totalW = sum(w)
        self.prefixW = [0] * len(w)
        self.prefixW[0] = w[0]
        for i in range(1, len(w)):
            self.prefixW[i] = self.prefixW[i - 1] + w[i]

    def pickIndex(self) -> int:
        rand = randrange(1, self.totalW + 1)
        lo, hi = 0, len(self.prefixW)
        while lo < hi:
            mid = (lo + hi) >> 1
            if self.prefixW[mid] < rand:
                lo = mid + 1
            else:
                hi = mid
        return lo
        

            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()