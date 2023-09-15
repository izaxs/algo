# 691. Stickers to Spell Word

# We are given n different types of stickers. Each sticker has a lowercase English word on it.

# You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

# Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

# Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

# Constraints:

#     n == stickers.length
#     1 <= n <= 50
#     1 <= stickers[i].length <= 10
#     1 <= target.length <= 15
#     stickers[i] and target consist of lowercase English letters.

class Solution:
    ORDINAL = 26
    BASE = ord('a')
    MAX = 1 << 31

    # TLE, 62 / 101 testcases passed
    def minStickers3(self, stickers: list[str], target: str) -> int:
        if not target: return 0
        useFulChars = set(target)

        def charOrd(c: str) -> int: return ord(c) - self.BASE

        def charsCount(sticker: str) -> tuple[list[int], int]:
            order = [0] * self.ORDINAL
            usefulNess = 0
            for c in sticker:
                if c in useFulChars:
                    order[charOrd(c)] += 1
                    usefulNess += 1
            return order, usefulNess

        def update(available: list[int], op: int, newChars: list[int]):
            for i in range(len(available)): available[i] += op * newChars[i]

        def charsRankMap(charsRank: list[int]) -> list[list[int]]:
            rankMap: list[list[int]] = [[]] * self.ORDINAL # int -> index of charsList
            for c in set(target):
                cOrd = charOrd(c)
                cRank = rankMap[cOrd]
                for i, chars in enumerate(charsList):
                    if chars[cOrd]: cRank.append(i)
                cRank.sort(key=lambda x: -charsRank[x])
            return rankMap

        countResult = [charsCount(stk) for stk in stickers]
        charsList = [c for c, _ in countResult]
        charsRank = [r for _, r in countResult]
        rankMap = charsRankMap(charsRank)

        minStkCount = self.MAX

        def trySolve(curCount: int, charAt: int, availableChars: list[int]):
            nonlocal minStkCount
            if curCount >= minStkCount: return
            if charAt == len(target):
                if curCount < minStkCount: 
                    minStkCount = curCount
                return
            curOrd = charOrd(target[charAt])
            if availableChars[curOrd] > 0:
                availableChars[curOrd] -= 1
                trySolve(curCount, charAt + 1, availableChars)
                availableChars[curOrd] += 1
            else:
                for charsListIndex in rankMap[curOrd]:
                    chars = charsList[charsListIndex]
                    if not chars[curOrd]: continue
                    update(availableChars, +1, chars)
                    trySolve(curCount + 1, charAt, availableChars)
                    update(availableChars, -1, chars)

        trySolve(0, 0, [0] * self.ORDINAL)
        return minStkCount if minStkCount != self.MAX else -1


    def minStickers2(self, stickers: list[str], target: str) -> int:
        if not target: return 0
        def charOrd(c: str) -> int: return ord(c) - self.BASE

        def charsCount(sticker: str) -> list[int]:
            order = [0] * self.ORDINAL
            for c in sticker: order[charOrd(c)] += 1
            return order

        def update(available: list[int], op: int, newChars: list[int]):
            for i in range(len(available)): available[i] += op * newChars[i]

        def rank() -> list[list[int]]:
            rankMap: list[list[int]] = [[]] * self.ORDINAL # int -> index of charsList
            for c in set(target):
                cOrd = charOrd(c)
                cRank = rankMap[cOrd]
                for i, chars in enumerate(charsList):
                    if chars[cOrd]: cRank.append(i)
                # cRank.sort(key=lambda x: charsList[x][cOrd], reverse=True)
            return rankMap
                
                

        charsList = [charsCount(stk) for stk in stickers]
        rankMap = rank()
        minStkCount = self.MAX

        def trySolve(curCount: int, charAt: int, availableChars: list[int]):
            nonlocal minStkCount
            if curCount >= minStkCount: return
            if charAt == len(target):
                if curCount < minStkCount: 
                    minStkCount = curCount
                return
            curOrd = charOrd(target[charAt])
            if availableChars[curOrd] > 0:
                availableChars[curOrd] -= 1
                trySolve(curCount, charAt + 1, availableChars)
                availableChars[curOrd] += 1
            else:
                for charsListIndex in rankMap[curOrd]:
                    chars = charsList[charsListIndex]
                    if not chars[curOrd]: continue
                    update(availableChars, +1, chars)
                    trySolve(curCount + 1, charAt, availableChars)
                    update(availableChars, -1, chars)

        trySolve(0, 0, [0] * self.ORDINAL)
        return minStkCount if minStkCount != self.MAX else -1

    # TLE exceed, 98 / 101 testcases passed
    def minStickers1(self, stickers: list[str], target: str) -> int:
        if not target: return 0
        def charOrd(c: str) -> int: return ord(c) - self.BASE

        def charsCount(sticker: str) -> list[int]:
            order = [0] * self.ORDINAL
            for c in sticker: order[charOrd(c)] += 1
            return order

        def update(available: list[int], op: int, newChars: list[int]):
            for i in range(len(available)): available[i] += op * newChars[i]

        charsList = [charsCount(stk) for stk in stickers]
        minStkCount = self.MAX

        def trySolve(curCount: int, charAt: int, availableChars: list[int]):
            nonlocal minStkCount
            if curCount >= minStkCount: return
            if charAt == len(target):
                if curCount < minStkCount: 
                    minStkCount = curCount
                return
            curOrd = charOrd(target[charAt])
            if availableChars[curOrd] > 0:
                availableChars[curOrd] -= 1
                trySolve(curCount, charAt + 1, availableChars)
                availableChars[curOrd] += 1
            else:
                for chars in charsList:
                    if not chars[curOrd]: continue
                    update(availableChars, +1, chars)
                    trySolve(curCount + 1, charAt, availableChars)
                    update(availableChars, -1, chars)

        trySolve(0, 0, [0] * self.ORDINAL)
        return minStkCount if minStkCount != self.MAX else -1
    
    # Other people's solution :(
    def minStickers0(self, stickers: list[str], target: str) -> int:
        import collections
        from typing import Counter

        stickersCount: list[Counter[str]] = [collections.Counter(s) for s in stickers if set(s) & set(target)]
        self.dpMap: dict[str, int] = {}
        def dfs(target):
            if not target: return 0
            if target in self.dpMap: return self.dpMap[target]
            cnt, res = collections.Counter(target), float('inf')
            for c in stickersCount: # traverse the stickers to get new target
                if c[target[0]] == 0: continue # we can make sure the 1st letter will be removed to reduce the time complexity
                nextTarget = ''.join([s * t for (s, t) in (cnt - c).items()])
                nextResult = dfs(nextTarget)
                if nextResult != -1: res = min(res, 1 + nextResult)
            self.dpMap[target] = -1 if res == float('inf') else int(res)
            return self.dpMap[target]
        return dfs(target)
            

if __name__ == '__main__':
    r = Solution().minStickers0(["with","example","science"], "thehat")
    print(r)

            


        
        