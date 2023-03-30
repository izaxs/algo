from __future__ import annotations
from typing import Optional
import bisect

class TimeRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __lt__(self, other: TimeRange) -> bool:
        return self.start < other.start

    def overlaps(self, other: TimeRange) -> bool:
        return not (self.end <= other.start or other.end <= self.start)

class MeetingRoom:
    def __init__(self, id: str):
        self.id = id
        self.schedule = []

    def is_available(self, time_range: TimeRange) -> bool:
        for scheduled_meeting in self.schedule:
            if scheduled_meeting.overlaps(time_range):
                return False
        return True

    def book(self, time_range: TimeRange):
        bisect.insort(self.schedule, time_range)

class MeetingScheduler:
    def __init__(self, rooms: list[MeetingRoom]):
        self.rooms = rooms

    def schedule_meeting(self, time_range: TimeRange) -> Optional[str]:
        for room in self.rooms:
            if room.is_available(time_range):
                room.book(time_range)
                return room.id
        raise Exception("No meeting room available")


if __name__ == "__main__":
    room1 = MeetingRoom("Room 1")
    room2 = MeetingRoom("Room 2")
    scheduler = MeetingScheduler([room1, room2])

    meeting1 = TimeRange(9, 10)
    meeting2 = TimeRange(10, 11)
    meeting3 = TimeRange(9, 11)

    room_id1 = scheduler.schedule_meeting(meeting1)
    room_id2 = scheduler.schedule_meeting(meeting2)
    room_id3 = scheduler.schedule_meeting(meeting3)

    print(room_id1, room_id2, room_id3)