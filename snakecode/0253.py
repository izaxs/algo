import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        using: list[int] = []
        maxRooms = 0
        for i in intervals:
            while using and i[0] >= using[0]:
                heapq.heappop(using)
            heapq.heappush(using, i[1])
            maxRooms = max(maxRooms, len(using))
        return maxRooms

class Solution2:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        starts: list[int] = [0] * len(intervals)
        ends: list[int] = [0] * len(intervals)
        for i, v in enumerate(intervals):
            starts[i], ends[i] = v[0], v[1]
        starts.sort()
        ends.sort()
        s, e = 0, 0
        maxRooms, using = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                using += 1
                s += 1
            else:
                using -= 1
                e += 1
            maxRooms = max(maxRooms, using)
        return maxRooms


s = Solution()
intervals = [[0,30],[5,10],[15,20]]
r = s.minMeetingRooms(intervals)
print(r)