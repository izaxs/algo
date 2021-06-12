class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        expects: dict[int, int] = {k: 1} # {expectedSum: countMatched}
        curSum: int = 0
        result: int = 0
        for v in nums:
            curSum += v
            result += expects.get(curSum, 0)
            count = expects.get(k+curSum, 0)
            expects[k+curSum] = count + 1
        return result

    def subarraySum2(self, nums: list[int], k: int) -> int:
        from collections import Counter 
        counter = Counter({0: 1})
        curSum = result = 0
        for v in nums:
            curSum += v
            result += counter[curSum - k]
            counter[curSum] += 1
        return result