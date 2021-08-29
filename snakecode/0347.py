import heapq
from collections import Counter

class Solution:
    def countIt(self, nums: list[int]) -> tuple[dict[int, int], int]:
        res: dict[int, int] = {}
        maxFreq = 0
        for i in nums:
            freq = res.get(i, 0)+1
            maxFreq = max(maxFreq, freq)
            res[i] = freq
        return res, maxFreq

    def topKFrequent1(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=lambda x: counter[x])

    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        counter, _ = self.countIt(nums)
        return heapq.nlargest(k, counter.keys(), key=lambda x: counter[x])

    def topKFrequent3(self, nums: list[int], k: int) -> list[int]:
        counter, maxFreq = self.countIt(nums)
        freqs: list[list[int]] = [[] for _ in range(maxFreq+1)]
        for n, f in counter.items():
            freqs[f].append(n)
        res: list[int] = []
        for fs in reversed(freqs):
            for i in fs:
                if len(res) == k:
                    return res
                res.append(i)
        return res
