# Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 

# Constraints:
    # 0 <= n <= 30

class Solution:
    def fib(self, n: int) -> int:
        def fibGen():
            n1, n2 = 0, 1
            while True:
                yield n1
                n1, n2 = n2, n1+n2
        for i in fibGen():
            if n <= 0:
                return i
            n -= 1
        return 0
