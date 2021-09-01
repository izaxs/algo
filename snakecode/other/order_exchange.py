from __future__ import annotations
import heapq

class Order:
    def __init__(self, price: int) -> None:
        self.price = price

    def __eq__(self, other: Order) -> bool:
        return self.price == other.price

    def __repr__(self):
        return f'price: {self.price}'

class TimedOrder(Order):
    def __init__(self, price: int, timeStamp: int) -> None:
        super().__init__(price)
        self.timeStamp = timeStamp

    def __repr__(self):
        return f'price: {self.price}, timestamp: {self.timeStamp}'

class BuyOrder(TimedOrder):
    def __init__(self, price: int, timeStamp: int) -> None:
        super().__init__(price, timeStamp)

    def __lt__(self, other: BuyOrder) -> bool:
        return self.price > other.price

class SellOrder(TimedOrder):
    def __init__(self, price: int, timeStamp: int) -> None:
        super().__init__(price, timeStamp)

    def __lt__(self, other: SellOrder) -> bool:
        return self.price < other.price

class TradingSystem:
    def __init__(self) -> None:
        self.sellOrders: list[SellOrder] = []
        self.buyOrders: list[BuyOrder] = []

    def putBuyOrder(self, order: BuyOrder) -> tuple[bool, int]:
        print(f'Putting buy order {order}, System status:\n{self}')
        if self.sellOrders and self.sellOrders[0].price <= order.price:
            matched = heapq.heappop(self.sellOrders)
            return True, matched.price
        heapq.heappush(self.buyOrders, order)
        return False, 0

    def putSellOrder(self, order: SellOrder) -> tuple[bool, int]:
        print(f'Putting sell order {order}, System status:\n{self}')
        if self.buyOrders and self.buyOrders[0].price >= order.price:
            matched = heapq.heappop(self.buyOrders)
            return True, matched.price
        heapq.heappush(self.sellOrders, order)
        return False, 0

    def __repr__(self) -> str:
        return f'sell orders: {self.sellOrders}\nbuy order: {self.buyOrders}'

# Assume orders are sorted
class TimedTradingSystem(TradingSystem):
    def __init__(self, expirationTime: int) -> None:
        super().__init__()
        self.expirationTime = expirationTime

    def _orderIsValid(self, order: TimedOrder, actionTime: int) -> bool:
        return order.timeStamp + self.expirationTime >= actionTime

    def putBuyOrder(self, order: BuyOrder) -> tuple[bool, int]:
        while self.sellOrders and not self._orderIsValid(self.sellOrders[0], order.timeStamp):
            heapq.heappop(self.sellOrders)
        return super().putBuyOrder(order)

    def putSellOrder(self, order: SellOrder) -> tuple[bool, int]:
        while self.buyOrders and not self._orderIsValid(self.buyOrders[0], order.timeStamp):
            heapq.heappop(self.buyOrders)
        return super().putSellOrder(order)


system = TimedTradingSystem(10)
print('Result:', system.putBuyOrder(BuyOrder(20, 0)), '\n')
print('Result:', system.putBuyOrder(BuyOrder(30, 1)), '\n')
print('Result:', system.putBuyOrder(BuyOrder(25, 2)), '\n')
print('Result:', system.putSellOrder(SellOrder(34, 3)), '\n')
print('Result:', system.putSellOrder(SellOrder(36, 4)), '\n')
print('Result:', system.putSellOrder(SellOrder(32, 5)), '\n')
print('Result:', system.putBuyOrder(BuyOrder(32, 6)), '\n')
print('Result:', system.putBuyOrder(BuyOrder(32, 10)), '\n')
print('Result:', system.putSellOrder(SellOrder(37, 12)), '\n')
print('Result:', system.putBuyOrder(BuyOrder(35, 14)), '\n')
print('Result:', system.putSellOrder(SellOrder(31, 5)), '\n')
print('Result:', system.putBuyOrder(BuyOrder(40, 30)), '\n')
print('Result:', system.putSellOrder(SellOrder(10, 41)), '\n')
