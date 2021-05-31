import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        using, maxRooms = [], 0
        for i in intervals:
            while using and i[0] >= using[0]:
                heapq.heappop(using)
            heapq.heappush(using, i[1])
            maxRooms = max(maxRooms, len(using))
        return maxRooms

s = Solution()
intervals = [[0,30],[5,10],[15,20]]
r = s.minMeetingRooms(intervals)
print(r)