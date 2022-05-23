class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        last = [-1, -1]
        for i in intervals:
            if last[1] > i[0]:
                return False
            last = i
        return True