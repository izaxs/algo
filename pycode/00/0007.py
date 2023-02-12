# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        self.setLimit(x)
        result = 0
        while x != 0:
            tail: int = self.mod10(x)
            if self.overflow(result, tail):
                return 0
            result = result * 10 + tail
            x = self.divide10(x)
        return result

    def mod10(self, x: int) -> int:
        return x % 10 if x >= 0 else -(-x % 10)

    def divide10(self, x: int) -> int:
        return x // 10 if x >= 0 else -(-x // 10)

    def overflow(self, body: int, tail: int) -> bool:
        if self.sign > 0:
            return body > self.limitInt32Body or (body == self.limitInt32Body and tail > self.limitInt32Tail)
        else:
            return body < self.limitInt32Body or (body == self.limitInt32Body and tail < self.limitInt32Tail)

    def setLimit(self, x: int):
        self.sign: int = 1 if x >= 0 else -1
        self.limitInt32: int = 0x7fffffff if self.sign > 0 else -0x80000000
        self.limitInt32Tail: int = self.mod10(self.limitInt32)
        self.limitInt32Body: int = self.divide10(self.limitInt32)

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-10))