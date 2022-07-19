class Solution:
    def decodeString(self, s: str) -> str:
        stack: list[tuple[str, int]] = []
        curStr = ''
        i = 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                factor = 0
                while '0' <= s[i] <= '9':
                    factor = factor*10 + int(s[i])
                    i += 1
                stack.append((curStr, factor))
                curStr = ''
            elif s[i] == ']':
                preStr, factor = stack.pop()
                preStr += curStr*factor
                curStr = preStr
            else:
                curStr += s[i]
            i += 1
        return curStr

    def decodeString2(self, s: str) -> str:
        stack: list[tuple[str, int]] = []
        curStr, curNum = '', 0
        for c in s:
            if c == '[':
                stack.append((curStr, curNum))
                curStr, curNum = '', 0
            elif c == ']':
                preStr, factor = stack.pop()
                curStr = preStr+curStr*factor
            elif '0' <= c <= '9':
                curNum = curNum*10+int(c)
            else:
                curStr += c
        return curStr
