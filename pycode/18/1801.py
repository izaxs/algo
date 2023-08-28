# 1801. Number of Orders in the Backlog

# You are given a 2D integer array orders, where each orders[i] = [pricei, amounti, orderTypei] denotes that amounti orders have been placed of type orderTypei at the price pricei. The orderTypei is:

#     0 if it is a batch of buy orders, or
#     1 if it is a batch of sell orders.

# Note that orders[i] represents a batch of amounti independent orders with the same price and order type. All orders represented by orders[i] will be placed before all orders represented by orders[i+1] for all valid i.

# There is a backlog that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:

#     If the order is a buy order, you look at the sell order with the smallest price in the backlog. If that sell order's price is smaller than or equal to the current buy order's price, they will match and be executed, and that sell order will be removed from the backlog. Else, the buy order is added to the backlog.
#     Vice versa, if the order is a sell order, you look at the buy order with the largest price in the backlog. If that buy order's price is larger than or equal to the current sell order's price, they will match and be executed, and that buy order will be removed from the backlog. Else, the sell order is added to the backlog.

# Return the total amount of orders in the backlog after placing all the orders from the input. Since this number can be large, return it modulo 109 + 7.

# Constraints:

#     1 <= orders.length <= 105
#     orders[i].length == 3
#     1 <= pricei, amounti <= 109
#     orderTypei is either 0 or 1.
from __future__ import annotations
import heapq

class Order:
    def __init__(self, price, amount):
        self.price = price
        self.amount = amount

class BuyOrder(Order):
    def __init__(self, price, amount):
        super().__init__(price, amount)

    def __lt__(self, other: BuyOrder) -> bool:
        return other.price < self.price

class SellOrder(Order):
    def __init__(self, price, amount):
        super().__init__(price, amount)

    def __lt__(self, other: SellOrder) -> bool:
        return self.price < other.price

class Solution:
    def getNumberOfBacklogOrders(self, orders: list[list[int]]) -> int:
        def substract(cur: Order, pres: list) -> bool:
            if cur.amount <= 0: return True
            if pres[0].amount > cur.amount:
                pres[0].amount -= cur.amount
                cur.amount = 0
                return True
            else:
                used = heapq.heappop(pres)
                cur.amount -= used.amount
                return False
        
        sellOrders: list[SellOrder] = []
        buyOrders: list[BuyOrder] = []
        for odr in orders:
            if odr[2] == 0:
                buyOrder = BuyOrder(odr[0], odr[1])
                while sellOrders and sellOrders[0].price <= buyOrder.price:
                    if substract(buyOrder, sellOrders): break
                if buyOrder.amount > 0:
                    heapq.heappush(buyOrders, buyOrder)
            else:
                sellOrder = SellOrder(odr[0], odr[1])
                while buyOrders and buyOrders[0].price >= sellOrder.price:
                    if substract(sellOrder, buyOrders): break
                if sellOrder.amount > 0:
                    heapq.heappush(sellOrders, sellOrder)
        total = 0
        for o in sellOrders:
            total += o.amount
        for o in buyOrders:
            total += o.amount
        return total % (10**9 + 7)
    
    def getNumberOfBacklogOrders2(self, orders: list[list[int]]) -> int:
        buyOrders, sellOrders = [], []
        for price, amount, orderType in orders:
            if orderType: heapq.heappush(sellOrders, [price, amount])
            else: heapq.heappush(buyOrders, [-price, amount])
            while buyOrders and sellOrders and sellOrders[0][0] <= -buyOrders[0][0]:
                delta = min(buyOrders[0][1], sellOrders[0][1])
                buyOrders[0][1] -= delta
                sellOrders[0][1] -= delta
                if buyOrders[0][1] == 0: heapq.heappop(buyOrders)
                if sellOrders[0][1] == 0: heapq.heappop(sellOrders)
        total = 0
        for o in sellOrders: total += o[1]
        for o in buyOrders: total += o[1]
        return total % (10**9+7)
        
    

if __name__ == '__main__':
    orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
    result = Solution().getNumberOfBacklogOrders(orders)

                    
                        
                        