class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        merged: list[list[int]] = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged

    def merge2(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x: (x[0], x[1]))
        result: list[list[int]] = [intervals[0]]
        for it in intervals:
            if it[0] <= result[-1][1]:
                if it[1] > result[-1][1]: result[-1][1] = it[1]
            else: result.append(it)
        return result
