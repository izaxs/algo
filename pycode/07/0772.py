# Basic Calculator III

# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Constraints:

#     1 <= s <= 104
#     s consists of digits, '+', '-', '*', '/', '(', and ')'.
#     s is a valid expression.

class Solution:
    def calculate(self, s: str) -> int:
        ADD, SUB, MUL, DIV, LP, RP = '+', '-', '*', '/', '(', ')'

        def calculate_block(i: int, parseNumberOnly: bool) -> tuple[int, int]: # (value, next index)
            total, op, cur = 0, 1, 0
            while i < len(s):
                c = s[i]
                if c.isdecimal():
                    cur = cur*10+int(c)
                elif parseNumberOnly:
                    if c == LP:
                        cur, i = calculate_block(i+1, False)
                        return cur, i
                    return cur, i-1
                elif c == LP:
                    cur, i = calculate_block(i+1, False)
                elif c == RP:
                    return total+op*cur, i
                elif c == ADD:
                    total += op*cur
                    op, cur = 1, 0
                elif c == SUB:
                    total += op*cur
                    op, cur = -1, 0
                elif c == MUL:
                    nextVal, i = calculate_block(i+1, True)
                    cur *= nextVal
                elif c == DIV:
                    nextVal, i = calculate_block(i+1, True)
                    cur = int(cur / nextVal)
                i += 1
            return total+op*cur, i
        return calculate_block(0, False)[0]

if __name__ == "__main__":
    s = Solution()
    print(s.calculate("10/2/5"))
    print(s.calculate("2*(1+4)"))
    print(s.calculate("2*(5+5*2)"))
    print(s.calculate("2*(5+5*2)/3"))
    print(s.calculate("6/2+8"))
    print(s.calculate("6*2+8"))
    print(s.calculate("2*(5+5*2)/3+(6/2+8)"))
    print(s.calculate("(0-3)/4"))
    