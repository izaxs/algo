class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        beginSet: set[str] = set([beginWord])
        endSet: set[str] = set([endWord])
        ladder: set[str] = set(wordList)
        visited: set[str] = set()
        distance: int = 1
        while True:
            distance += 1
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            newSet: set[str] = set()
            for word in beginSet:
                for i, _ in enumerate(word):
                    for newC in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i]+newC+word[i+1:]
                        if newWord in endSet and newWord in ladder:
                            return distance
                        elif newWord in ladder and newWord not in visited:
                            newSet.add(newWord)
                            visited.add(newWord)
            if not newSet:
                return 0
            beginSet = newSet

if __name__ == '__main__':
    s = Solution()
    r = s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
    print(r)
