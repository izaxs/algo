# Basic Calculator

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Constraints:

#     1 <= s.length <= 3 * 105
#     s consists of digits, '+', '-', '(', ')', and ' '.
#     s represents a valid expression.
#     '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
#     '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
#     There will be no two consecutive operators in the input.
#     Every number and running calculation will fit in a signed 32-bit integer.

class Solution:
    def calculate(self, s: str) -> int:
        ADD, SUB, LP, RP = '+', '-', '(', ')'

        stack: list[tuple[int, int]] = [(1, 0)] # (op, value)
        op, cur = 1, 0
        s, i = s, 0
        while i < len(s):
            if s[i].isdecimal():
                cur = cur*10+int(s[i])
            elif s[i] == ADD:
                stack[-1] = stack[-1][0], stack[-1][1]+op*cur
                op, cur = 1, 0
            elif s[i] == SUB:
                stack[-1] = stack[-1][0], stack[-1][1]+op*cur
                op, cur = -1, 0
            elif s[i] == LP:
                stack.append((op, cur))
                op, cur = 1, 0
            elif s[i] == RP:
                stack[-1] = stack[-1][0], stack[-1][1]+op*cur
                op, cur = stack.pop()
            i += 1
        return stack[-1][1]+op*cur

    def calculate_fast(self, s: str) -> int:
        ADD, SUB, LP, RP = '+', '-', '(', ')'

        stack: list[tuple[int, int]] = [] # (op, value)
        preOp, preVal, curOp, curVal, i = 1, 0, 1, 0, 0
        while i < len(s):
            if s[i].isdecimal():
                curVal = curVal*10+int(s[i])
            elif s[i] == ADD:
                preVal += curOp*curVal
                curOp, curVal = 1, 0
            elif s[i] == SUB:
                preVal += curOp*curVal
                curOp, curVal = -1, 0
            elif s[i] == LP:
                stack.append((preOp, preVal))
                preOp, preVal, curOp, curVal = curOp, curVal, 1, 0
            elif s[i] == RP:
                preVal += curOp*curVal
                prePreOp, prePreVal = stack.pop()
                preOp, preVal, curOp, curVal = prePreOp, prePreVal+preOp*preVal, 1, 0
            i += 1
        return preVal+curOp*curVal

    def calculate_recur(self, s: str) -> int:
        ADD, SUB, LP, RP = '+', '-', '(', ')'
        def helper(s: str, i: int) -> tuple[int, int]: # (value, i)
            preVal, curOp, curVal = 0, 1, 0
            while i < len(s):
                if s[i].isdecimal():
                    curVal = curVal*10+int(s[i])
                elif s[i] == ADD:
                    preVal += curOp*curVal
                    curOp, curVal = 1, 0
                elif s[i] == SUB:
                    preVal += curOp*curVal
                    curOp, curVal = -1, 0
                elif s[i] == LP:
                    curVal, i = helper(s, i+1)
                elif s[i] == RP:
                    return preVal+curOp*curVal, i
                i += 1
            return preVal+curOp*curVal, i
        return helper(s, 0)[0]
                


if __name__ == '__main__':
    s = Solution()
    print(s.calculate_recur(" 2-1 + 2 "))
    print(s.calculate_fast('(1 + 1)-3'))
    print(s.calculate_fast(' (1+(4+5+2)-3)+(6+9)'))
    
    
