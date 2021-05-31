class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        orderMap = {c: i for i, c in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            i, minLen, isSmaller = 0, min(len(w1), len(w2)), False
            while i < minLen:
                cmp = orderMap[w1[i]] - orderMap[w2[i]]
                if cmp == 0:
                    i += 1
                    continue
                if cmp < 0:
                    isSmaller = True
                    break
                if cmp > 0:
                    return False
            if not isSmaller and len(w1) > len(w2):
                return False
        return True

s = Solution()
s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")