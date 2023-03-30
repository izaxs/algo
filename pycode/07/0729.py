# My Calendar I

# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendar class:

#     MyCalendar() Initializes the calendar object.
#     boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

# Constraints:

#     0 <= start < end <= 109
#     At most 1000 calls will be made to book.

from __future__ import annotations

class BookedTime:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def __lt__(self, other: BookedTime):
        return self.end <= other.start

class MyCalendar:

    def __init__(self):
        self.bookedTime = None

    def book(self, start: int, end: int) -> bool: # type: ignore
        toBook = BookedTime(start, end)
        if not self.bookedTime:
            self.bookedTime = toBook
            return True
        booked = self.bookedTime
        while booked:
            if booked < toBook:
                if not booked.right:
                    booked.right = toBook # type: ignore
                    return True
                booked = booked.right
            elif toBook < booked:
                if not booked.left:
                    booked.left = toBook # type: ignore
                    return True
                booked = booked.left
            else:
                return False



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

actions = [[],[20,29],[13,22],[44,50],[1,7],[2,10],[14,20],[19,25],[36,42],[45,50],[47,50],[39,45],[44,50],[16,25],[45,50],[45,50],[12,20],[21,29],[11,20],[12,17],[34,40],[10,18],[38,44],[23,32],[38,44],[15,20],[27,33],[34,42],[44,50],[35,40],[24,31]]
obj = MyCalendar()
for action in actions:
    if action: obj.book(*action)
        



