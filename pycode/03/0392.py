class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        dp1: list[bool] = [True]*(len(t)+1)
        for i in range(len(s)):
            dp2: list[bool] = [False]*(len(t)+1)
            for j in range(i+1, len(dp2)):
                if dp2[j-1] or (s[i] == t[j-1] and dp1[j-1]):
                    dp2[j] = True
            dp1 = dp2
        return dp1[-1]

    def isSubsequence2(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        i, j = 0, 0
        while True:
            if i >= len(s):
                return True
            if j >= len(t):
                return False
            if s[i] == t[j]:
                i += 1
            j += 1

    def isSubsequence3(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def isSubsequence4(self, s: str, t: str) -> bool:
        tIter = iter(t)
        return all(cs in tIter for cs in s)


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
