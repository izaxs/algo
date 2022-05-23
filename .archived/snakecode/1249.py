class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openCount, closeCount = 0, 0
        for c in s:
            closeCount += int(c == ')')
        result = ''
        for c in s:
            if c == '(':
                if openCount == closeCount: continue
                openCount += 1
            elif c == ')':
                closeCount -= 1
                if openCount == 0: continue
                openCount -= 1
            result += c
        return result

    def minRemoveToMakeValid2(self, s: str) -> str:
        openCount, closeCount = 0, 0
        for c in s:
            closeCount += int(c == ')')
        result = list(s)
        for i, c in enumerate(s):
            if c == '(':
                if openCount == closeCount:
                    result[i] = ''
                    continue
                openCount += 1
            elif c == ')':
                closeCount -= 1
                if openCount == 0:
                    result[i] = ''
                    continue
                openCount -= 1
        return ''.join(result)

    def minRemoveToMakeValid3(self, s: str) -> str:
        stk: list[str] = []
        cur = ''
        for c in s:
            if c == '(':
                stk.append(cur)
                cur = ''
            elif c == ')':
                if stk: cur = f'{stk.pop()}({cur})'
            else:
                cur += c
        cur = ''.join(stk) + cur
        return cur
            

if __name__ == '__main__':
    s = Solution()
    # r = s.minRemoveToMakeValid("lee(t(c)o)de)")
    r = s.minRemoveToMakeValid("a)b(c)d")
    print(r)