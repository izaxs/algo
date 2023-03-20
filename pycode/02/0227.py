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
    
    def calculate2(self, s: str) -> int:
        def parseNumber(s: str, i: int) -> tuple[int, int]:
            num = 0
            while i < len(s) and s[i].isspace():
                i += 1
            while i < len(s) and s[i].isdecimal(): 
                num = num*10+int(s[i])
                i += 1
            return (num, i)
        
        s, i = '+' + s + '+', 0
        res, cur, op = 0, 0, 1
        while i < len(s):
            if s[i] == '+' or s[i] == '-':
                res = res+op*cur
                op = 1 if s[i] == '+' else -1
                cur, i = parseNumber(s, i+1)
            elif s[i] == '*':
                num, i = parseNumber(s, i+1)
                cur *= num
            elif s[i] == '/':
                num, i = parseNumber(s, i+1)
                cur //= num
            else: i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    s.calculate2('3/2')
    s.calculate2('3+ 5/2')
    # s.calculate2("3+2*2")
    # s.calculate2('3+5 *2-4 ')