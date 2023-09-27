class Solution:
    def clear(self, word: str) -> str:
        stk: list[str] = []
        i = 0
        while i < len(word):
            c = word[i]
            if not (len(stk) >= 2 and c == stk[-1] and c == stk[-2]):
                stk.append(c)
                i += 1
                continue
            while stk and stk[-1] == c:
                stk.pop()
            i += 1
            while i < len(word) and word[i] == c:
                i += 1
        return ''.join(stk)


if __name__ == '__main__':
    s = Solution()
    assert s.clear('aabbbbaccddddc') == ''
    assert s.clear('aaaaaa') == ''
    assert s.clear('aabba') == 'aabba'
    assert s.clear('abbbabba') == 'aabba'