class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aIndex: int = len(a) - 1
        bIndex: int = len(b) - 1
        result, carry = '', 0
        while aIndex >= 0 or bIndex >= 0:
            if aIndex >= 0:
                carry = carry + 1 if a[aIndex] == '1' else carry
                aIndex -= 1
            if bIndex >= 0:
                carry = carry + 1 if b[bIndex] == '1' else carry
                bIndex -= 1
            result = '0' + result if carry % 2 == 0 else '1' + result
            carry //= 2
        result = result if carry % 2 == 0 else '1' + result
        return result

    def addBinary2(self, a: str, b: str) -> str:
        aChars: list[str] = list(a)
        bChars: list[str] = list(b)
        result = ''
        carry = 0
        while aChars or bChars or carry:
            if aChars:
                carry += int(aChars.pop())
            if bChars:
                carry += int(bChars.pop())
            result = str(carry % 2) + result
            carry //= 2
        return result

if __name__ == '__main__':
    s = Solution()
    r = s.addBinary('100', '100')
    print(r)