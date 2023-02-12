# Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Constraints:

#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {'{': '}', '[': ']', '(': ')'}
        stack: list[str] = []
        for c in s:
            if c in symbols:
                stack.append(symbols[c])
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        return not stack
