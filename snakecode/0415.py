class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i1, i2 = len(num1) - 1, len(num2) - 1
        res, carry = [], 0
        while i1 >= 0 or i2 >= 0:
            if i1 >= 0:
                carry += int(num1[i1])
                i1 -= 1
            if i2 >= 0:
                carry += int(num2[i2])
                i2 -= 1
            res.append(carry % 10)
            carry //= 10
        if carry:
            res.append(carry)
        return ''.join(str(i) for i in reversed(res))