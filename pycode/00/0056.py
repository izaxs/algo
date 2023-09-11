# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Constraints:

#     1 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti <= endi <= 104

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

    def merge3(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        result: list[list[int]] = list([intervals[0]])
        for lo, hi in intervals[1:]:
            if lo > result[-1][1]: result.append([lo, hi])
            elif hi > result[-1][1]: result[-1][1] = hi
        return result
