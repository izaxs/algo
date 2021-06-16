class Solution:

    pad = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        if not digits:
            return res
        res.append('')
        for d in digits:
            newRes = []
            for comb in res:
                for alpha in self.pad[int(d)]:
                    newRes.append(comb + alpha)
            res = newRes
        return res
