# Happy Number

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.

# Constraints:

#     1 <= n <= 231 - 1

class Solution:
    def isHappy(self, n: int) -> bool:
        seen: set[int] = set()
        while n != 1:
            if n in seen: return False
            seen.add(n)
            nextN = 0
            while n > 0:
                nextN += (n % 10)**2
                n //= 10
            n = nextN
        return True