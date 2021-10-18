class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        expects: dict[int, int] = {k: 1}  # {expectedSum: countMatched}
        curSum: int = 0
        result: int = 0
        for v in nums:
            curSum += v
            result += expects.get(curSum, 0)
            count = expects.get(k+curSum, 0)
            expects[k+curSum] = count + 1
        return result

    # def subarraySum2(self, nums: list[int], k: int) -> int:
    #     curSum, result = 0, 0
    #     preSum: dict[int, int] = {0: 1}
    #     for n in nums:
    #         curSum += n
    #         # preSum is used for later iterations, can not affect this round
    #         preSum[curSum] = preSum.get(curSum, 0)+1
    #         result += preSum.get(curSum-k, 0)
    #     return result

    def subarraySum3(self, nums: list[int], k: int) -> int:
        preSums = {0: 1}
        curSum, count = 0, 0
        for n in nums:
            curSum += n
            count += preSums.get(curSum-k, 0)
            preSums[curSum] = preSums.get(curSum, 0)+1
        return count