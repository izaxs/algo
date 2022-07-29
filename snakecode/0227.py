class Solution:
    def calculate(self, s: str) -> int:
        signs = ('+', '-', '*', '/')
        stack: list[int] = []
        num: int = 0
        sign: str = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num*10+int(c)
            if c in signs or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    preNum = stack.pop()
                    preSign = 1 if preNum >= 0 else -1
                    preNum = abs(preNum)
                    preNum //= num
                    preNum *= preSign
                    stack.append(preNum)
                sign = c
                num = 0
        return sum(stack)


s = Solution()
print(s.calculate('3+5 *2-4 '))