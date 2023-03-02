from __future__ import annotations
import heapq 

class Item:
    def __init__(self, symbol: str, price: int, nums: int, col = None) -> None:
        self.symbol = symbol
        self.price = price
        self.nums = nums
        self.collateral = col
    
    # Order:
    # symbol doesn't end with O is larger
    # price reversed
    def __lt__(self, other: Item):
        if (self.symbol[-1] == 'O') ^ (other.symbol[-1] == 'O'):
            return self.symbol >= other.symbol
        if self.symbol[-1] == 'O':
            return False
        return True

    def __str__(self):
        return f'{self.symbol=}, {self.price=}, {self.nums=}, {self.collateral=}'

stocks = [
    Item('applO', 100, 5),
    Item('apple', 60, 6),
    Item('gg', 80, 3),
]

heapq.heapify(stocks)
for _ in range(len(stocks)):
    print(heapq.heappop(stocks))
