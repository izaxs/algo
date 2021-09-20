# Two Sigma HackerRank
class B:
    def __init__(self, bidderId: int, shares: int, price: int, ts: int) -> None:
        self.id = bidderId
        self.shares = shares
        self.price = price
        self.ts = ts

def bid_losers(bids: list[B], total: int) -> list[int]:
    remain = set((x.id for x in bids))
    if total <= 0: return list(remain)
    bids.sort(key=lambda x: (-x.price, x.ts))
    cur = 0
    while cur < len(bids):
        n = 1
        deduct = 0
        while cur+n < len(bids) and bids[cur+n].price == bids[cur].price:
            deduct += bids[cur+n].shares
            n += 1
        if n == 1:
            if bids[cur].shares > 0:
                remain.discard(bids[cur].id)
            total -= bids[cur].shares
        else:
            if total < n:
                for i in range(total):
                    remain.discard(bids[cur+i].id)
                return list(remain)
            else:
                for i in range(n):
                    remain.discard(bids[cur+i].id)
            total -= deduct
        if total <= 0:
            break
        cur += n
    return list(remain)

bids = [B(4, 2, 101, 0), B(5, 1, 99, 1), B(0, 4, 99, 3), B(2, 4, 105, 3), B(5, 2, 99, 3), B(1, 3, 99, 4)]
total = 13
print(bid_losers(bids, total))