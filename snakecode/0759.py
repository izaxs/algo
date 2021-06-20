from typing import Any

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"({self.start}, {self.end})"

class Solution:
    def employeeFreeTime(self, schedule: list[list[Interval]]) -> list[Interval]:
        intervals = [i for person in schedule for i in person]
        intervals.sort(key=lambda x: (x.start, x.end))
        freeTime: list[Interval] = []
        lastEnd: int = intervals[0].end
        for i in intervals[1:]:
            if i.start > lastEnd:
                freeTime.append(Interval(lastEnd, i.start))
            lastEnd = max(lastEnd, i.end)
        return freeTime

if __name__ == '__main__':
    s = Solution()
    inputs: list[list[Any]] = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
    for i, person in enumerate(inputs):
        for j, interval in enumerate(person):
            inputs[i][j] = Interval(interval[0], interval[1])
    r = s.employeeFreeTime(inputs)
    print(r)
