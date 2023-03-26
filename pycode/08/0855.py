# Exam Room

# There is an exam room with n seats in a single row labeled from 0 to n - 1.

# When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number 0.

# Design a class that simulates the mentioned exam room.

# Implement the ExamRoom class:

#     ExamRoom(int n) Initializes the object of the exam room with the number of the seats n.
#     int seat() Returns the label of the seat at which the next student will set.
#     void leave(int p) Indicates that the student sitting at seat p will leave the room. It is guaranteed that there will be a student sitting at seat p.

# Constraints:

#     1 <= n <= 10^9
#     It is guaranteed that there is a student sitting at seat p.
#     At most 104 calls will be made to seat and leave.

# Bad for large n
class ExamRoom_Slow:
    def __init__(self, n: int):
        self.seats = [0]*n
        self.N = n
        self.count = 0

    def distLessThan(self, lo1: int, hi1: int, lo2: int, hi2: int) -> bool:
        if self.seats[lo1] == 0 or self.seats[hi1] == 0: d1 = hi1-lo1
        else: d1 = (hi1 - lo1) >> 1
        if self.seats[lo2] == 0 or self.seats[hi2] == 0: d2 = hi2-lo2
        else: d2 = (hi2 - lo2) >> 1
        return d1 < d2

    def seat(self):
        self.count += 1
        if self.count == 1:
            self.seats[0] = 1
            return 0
        maxLo, maxHi = 0, 0
        lo, hi = 0, 0
        for hi in range(self.N):
            if self.seats[hi] == 1 or hi == self.N-1:
                if self.distLessThan(maxLo, maxHi, lo, hi):
                    maxLo, maxHi = lo, hi
                lo = hi
        if self.seats[maxLo] == 0:
            self.seats[0] = 1
            return 0
        if self.seats[maxHi] == 0:
            self.seats[maxHi] = 1
            return maxHi
        mid = (maxLo + maxHi) >> 1
        self.seats[mid] = 1
        return mid
        

    def leave(self, p):
        self.seats[p] = 0
        self.count -= 1

# Normal solution
import include
from bisect import insort
from printer import monitor

class ExamRoom_Normal:
    def __init__(self, n: int):
        self.seats: list[int] = []
        self.HI = n - 1

    @monitor
    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        leftOpenDist, rightOpenDist = self.seats[0], self.HI - self.seats[-1]
        maxLo = maxHi = lastIdx = self.seats[0]
        for i in self.seats:
            if ((maxHi - maxLo) >> 1) < ((i - lastIdx) >> 1):
                maxLo, maxHi = lastIdx, i
            lastIdx = i
        closedDist = (maxHi - maxLo) >> 1
        maxDist = max(closedDist, leftOpenDist, rightOpenDist)
        if maxDist == leftOpenDist:
            self.seats.insert(0, 0)
            return 0
        elif maxDist == closedDist:
            mid = (maxLo + maxHi) >> 1
            insort(self.seats, mid)
            return mid
        else:
            self.seats.append(self.HI)
            return self.HI

    @monitor
    def leave(self, p):
        self.seats.remove(p)


if __name__ == "__main__":
    import sys
    print(sys.path)
    r = ExamRoom_Normal(4)  
    r.seat()
    r.seat()
    r.seat()
    r.seat()
    r.leave(1)
    r.leave(3)
    r.seat()