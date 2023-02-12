# Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Constraints:

#     0 <= digits.length <= 4
#     digits[i] is a digit in the range ['2', '9'].


class Solution:

    pad = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits: str) -> list[str]:
        res: list[str] = []
        if not digits:
            return res
        res.append('')
        for d in digits:
            newRes: list[str] = []
            for comb in res:
                for alpha in self.pad[int(d)]:
                    newRes.append(comb + alpha)
            res = newRes
        return res
