# 346. Moving Average from Data Stream

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

#     MovingAverage(int size) Initializes the object with the size of the window size.
#     double next(int val) Returns the moving average of the last size values of the stream.

# Constraints:

#     1 <= size <= 1000
#     -105 <= val <= 105
#     At most 104 calls will be made to next.

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.data: deque[int] = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.data) == self.size:
            removed = self.data.popleft()
            self.sum -= removed
        self.data.append(val)
        self.sum += val
        return self.sum / len(self.data)