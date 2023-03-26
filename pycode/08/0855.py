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

# Fast solution
import heapq

class ExamRoom:
    def __init__(self, n: int):
        self.N = n
        self.seats: list[Slot] = []
        self.slotsRightSide: dict[int, Slot] = {}
        self.slotsLeftSide: dict[int, Slot] = {}
        self.seats.append(Slot(None, None, n))
    
    @monitor
    def seat(self):
        while True:
            slot = heapq.heappop(self.seats)
            if slot.isValid:
                break
        if slot.lo == None:
            slot.lo = 0
            self.slotsLeftSide[0] = slot
            heapq.heappush(self.seats, slot)
            return 0
        if slot.hi == None:
            slot.hi = slot.N - 1
            self.slotsRightSide[slot.N - 1] = slot
            heapq.heappush(self.seats, slot)
            return slot.N - 1
        mid = (slot.lo + slot.hi) >> 1
        leftSlot = Slot(slot.lo, mid, slot.N)
        rightSlot = Slot(mid, slot.hi, slot.N)
        self.slotsLeftSide[slot.lo], self.slotsLeftSide[mid] = leftSlot, rightSlot
        self.slotsRightSide[mid], self.slotsRightSide[slot.hi] = leftSlot, rightSlot
        heapq.heappush(self.seats, leftSlot)
        heapq.heappush(self.seats, rightSlot)
        return mid

    def leave(self, p):
        slot = Slot(None, None, self.N)
        leftSlot = self.slotsRightSide.pop(p, None)
        rightSlot = self.slotsLeftSide.pop(p, None)
        if leftSlot:
            slot.lo = leftSlot.lo # type: ignore
            leftSlot.isValid = False
        if rightSlot:
            slot.hi = rightSlot.hi # type: ignore
            rightSlot.isValid = False
        if slot.lo:
            self.slotsLeftSide[slot.lo] = slot
        if slot.hi:
            self.slotsRightSide[slot.hi] = slot
        heapq.heappush(self.seats, slot)

class Slot:
    def __init__(self, lo, hi, N):
        self.lo = lo # lo seat index
        self.hi = hi # hi seat index
        self.N = N
        self.isValid = True

    def nextDist(self) -> int:
        if self.lo == None and self.hi == None:
            return self.N
        if self.lo == None:
            return self.hi
        if self.hi == None:
            return self.N - 1 - self.lo
        return (self.hi - self.lo) >> 1

    # To be sorted in min heap, the larger the nextDist, the smaller the slot
    def __lt__(self, other) -> bool:
        cmp = self.nextDist() - other.nextDist()
        if cmp != 0: return cmp > 0
        if self.lo == None: return True
        if other.lo == None: return False
        return self.lo < other.lo

    def __repr__(self):
        return f"Slot({self.lo}, {self.hi})"


if __name__ == "__main__":
    r = ExamRoom(10)  
    r.seat()
    r.seat()
    r.seat()
    r.seat()
    r.leave(4)
    r.seat()