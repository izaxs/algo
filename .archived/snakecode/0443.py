class Solution2:
    def compress(self, chars: list[str]) -> int:
        # res: the current result group head; cur: the index of first char of current group
        i, res, cur = 0, 0, 0
        while i < len(chars):
            if i + 1 == len(chars) or chars[i] != chars[i + 1]:
                chars[res] = chars[cur]
                res += 1
                if i > cur: # insert length into chars list
                    for c in str(i - cur + 1):
                        chars[res] = c
                        res += 1
                cur = i + 1
            i += 1
        return res

class Solution1:
    def compress(self, chars: list[str]) -> int:
        i, head, curChar, curLen = 0, 0, '', 0
        while i <= len(chars):
            if i == len(chars) or (curChar and curChar != chars[i]):
                head += self.setLen(chars, head, curChar, curLen)
                if i < len(chars): # Continue if there's more
                    curChar = chars[i]
                    curLen = 1
            elif curChar == chars[i]:
                curLen += 1
            else: # Init
                curChar = chars[i]
                curLen = 1
            i += 1
        return head

    def setLen(self, chars: list[str], head: int, curChar: str, curLen: int) -> int:
        chars[head] = curChar
        if curLen == 1:
            return 1
        lenStr = list(str(curLen))
        for c in lenStr:
            head += 1
            chars[head] = c
        return len(lenStr) + 1