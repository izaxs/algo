# There are n cities. Some of them are connected, while some are not.
# If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

class Solution:
    def findProvinceNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        graph: dict[int, list[int]] = {}
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if not isConnected[i][j]: continue
                nbs = graph.setdefault(i, [])
                nbs.append(j)
        visited: list[bool] = [False]*n

        def dfs(n: int) -> bool:
            if visited[n]: return False
            visited[n] = True
            for nb in graph.get(n, []):
                dfs(nb)
            return True

        res = 0
        for i in range(n):
            if dfs(i): res += 1
        return res

    def findProvinceNum2(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited: list[bool] = [False]*n

        def dfs(cur: int):
            if visited[cur]: return
            visited[cur] = True
            for i in range(n):
                if isConnected[cur][i]: dfs(i)

        res = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        return res

s = Solution()
connected = [[1,1,0],[1,1,0],[0,0,1]]
print(s.findProvinceNum(connected))