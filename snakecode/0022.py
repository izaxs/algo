class Solution3:
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                yield from generate(p + '(', left-1, right)
                yield from generate(p + ')', left, right-1)
        return list(generate('', n, n))

class Solution2:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)


class Solution1:
    def generateParenthesis(self, n: int) -> list[str]:
        if n <= 0:
            return []
        res = ['']
        res = self.helper(res, n, 0, True)
        return res

    def helper(self, res: List[str], n: int, remain: int, add: bool) -> list[str]:
        if n == 0 and remain == 0 and add: # End of recursion
            return res
        if (add and n == 0) or (not add and remain == 0): # Reject two cases
            return []
        curRes = []
        for s in res:
            if add:
                curRes.append(s + '(')
                remain += 1
                n -= 1
            else:
                curRes.append(s + ')')
                remain -= 1
        nextRes = []
        res1 = self.helper(curRes, n, remain, True)
        res2 = self.helper(curRes, n, remain, False)
        nextRes.extend(res1)
        nextRes.extend(res2)
        return nextRes