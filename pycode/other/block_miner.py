# Enter your code here. Read input from STDIN. Print output to STDOUT
# {
#   "transactionID": "A",
#   "fee": 100,
#   "size": 25
# },
# {
#   "transactionID": "B",
#   "fee": 120,
#   "size": 20
# },
# {
#   "transactionID": "C",
#   "fee": 30,
#   "size": 10
# },
# {
#   "transactionID": "D",
#   "fee": 400,
#   "size": 50
# },
# {
#   "transactionID": "E",
#   "fee": 250,
#   "size": 25
# }
#
# Expected: transaction B, transaction D, transaction E

# fees: [60, 100, 150]
# size: [40, 60, 61]
# block: 100

# greedy: 150, 61
# remain: 39

# 60 + 100 = 160

BLOCKSIZE = 100

class Transaction:
    def __init__(self, tid: str, fee: int, size: int):
        self.tid = tid
        self.size = size
        self.fee = fee

def mine_block(mempool: list[Transaction]) -> list[str]:
    N = len(mempool)
    results: dict[tuple[int, int], list[str]] = {}
    # dp[number of trans][blocksize]
    dp = [[-1 for _ in range(BLOCKSIZE+1)] for _ in range(N+1)]
    dp[0][0] = 0
    # remaining, nth
    results[(0, 0)] = []
    
    def helper(remaining: int, nth: int) -> int:
        if remaining <= 0 or nth == 0:
            dp[nth][0] = 0
            results[(max(remaining, 0), nth)] = []
            return 0
        if dp[nth][remaining] != -1:
            pass
        elif mempool[nth-1].size > remaining:
            dp[nth][remaining] = helper(remaining, nth-1)
            results[(remaining, nth)] = list(results[(remaining, nth-1)])
        else:
            notIncludingCur = helper(remaining, nth-1)
            includingCur = helper(remaining-mempool[nth-1].size, nth-1) + mempool[nth-1].fee
            if notIncludingCur >= includingCur:
                dp[nth][remaining] = notIncludingCur
                results[(remaining, nth)] = list(results[(remaining, nth-1)])
            else:
                dp[nth][remaining] = includingCur
                results[(remaining, nth)] = [mempool[nth-1].tid] + results[(remaining-mempool[nth-1].size, nth-1)]
        return dp[nth][remaining]
        
    helper(BLOCKSIZE, N)
    print(BLOCKSIZE, N, dp[N][BLOCKSIZE])
    return results[(BLOCKSIZE, N)]
    

# {
#   "transactionID": "A",
#   "fee": 100,
#   "size": 25
# },
# {
#   "transactionID": "B",
#   "fee": 120,
#   "size": 20
# },
# {
#   "transactionID": "C",
#   "fee": 30,
#   "size": 10
# },
# {
#   "transactionID": "D",
#   "fee": 400,
#   "size": 50
# },
# {
#   "transactionID": "E",
#   "fee": 250,
#   "size": 25
# }
#

if __name__ == "__main__":
    transactions = [
        Transaction("A", 100, 25),
        Transaction("B", 120, 76),
        Transaction("C", 30, 10),
        Transaction("D", 400, 50),
        Transaction("E", 150, 25),
    ]
    
    result = mine_block(transactions)
    print(result)