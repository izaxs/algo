# You are given a network of n nodes, labeled from 1 to n.
# You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node,
# and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k.
# Return the time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        Dist = tuple[int, int]
        RoutingMap = dict[int, list[Dist]]

        def buildRoute() -> RoutingMap:
            rMap: RoutingMap = {}
            for link in times:
                neighbors = rMap.setdefault(link[0], [])
                neighbors.append((link[2], link[1]))
            return rMap

        rMap = buildRoute()
        queue: list[Dist] = [(0, k)]
        toVisit: set[int] = set((i for i in range(1, n+1)))
        maxTime = 0
        while queue and toVisit:
            cur = heappop(queue)
            if cur[1] not in toVisit: continue
            toVisit.remove(cur[1])
            maxTime = max(maxTime, cur[0])
            for dist, nb in rMap.get(cur[1], []):
                heappush(queue, (cur[0]+dist, nb))
        if toVisit: return -1
        return maxTime
