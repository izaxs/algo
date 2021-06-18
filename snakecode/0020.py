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
