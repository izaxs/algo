# 57. Insert Interval

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Constraints:

#     0 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti <= endi <= 105
#     intervals is sorted by starti in ascending order.
#     newInterval.length == 2
#     0 <= start <= end <= 105

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if len(intervals) == 0: return [newInterval]
        if newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]: return intervals + [newInterval]

        result, i = [], 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
        result.extend(intervals[:i])

        loVal = min(intervals[i][0], newInterval[0])
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            i += 1
        hiVal = max(intervals[i-1][1], newInterval[1])
        result.append([loVal, hiVal])

        result.extend(intervals[i:])
        return result
    
    # Beautiful way
    def insert2(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        start, end = newInterval
        left, right = [], []
        for i in intervals:
            if i[1] < start: left.append(i)
            elif i[0] > end: right.append(i)
            else:
                start = min(start, i[0])
                end = max(end, i[1])
        return left + [[start, end]] + right
    
    # Frugal & Performant way
    def insert3(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        start, end = newInterval
        result, rightStart = [], len(intervals)
        for i, v in enumerate(intervals):
            if v[1] < start: 
                result.append(v)
            elif v[0] > end:
                rightStart = i
                break
            else:
                start = min(start, v[0])
                end = max(end, v[1])
        result.append([start, end])
        for i in range(rightStart, len(intervals)): result.append(intervals[i])
        return result
        

if __name__ == '__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    Solution().insert(intervals, newInterval)        
            


    
        