class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        totalMax = 0
        wordCounter: dict[str, int] = {}
        wordSet: set[str] = set(words)

        def tryCut(word: str) -> int:
            nonlocal totalMax
            if not word or word not in wordSet: return 0
            if word in wordCounter: return wordCounter[word]
            curMax = 0
            for i in range(len(word)):
                newWord = word[:i]+word[i+1:]
                n = tryCut(newWord)
                curMax = max(curMax, n+1)
            wordCounter[word] = curMax
            totalMax = max(totalMax, curMax)
            return curMax

        for w in words:
            tryCut(w)
        return totalMax
