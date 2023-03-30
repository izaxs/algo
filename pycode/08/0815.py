from collections import deque

class BusStop:
    def __init__(self) -> None:
        self.neighbors: set[int] = set()

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        graph: dict[int, BusStop] = {}
        for busRoute in routes: # Turns out time consuming
            for i in range(len(busRoute)):
                for j in range(i+1, len(busRoute)):
                    stop1 = graph.setdefault(busRoute[i], BusStop())
                    stop2 = graph.setdefault(busRoute[j], BusStop())
                    stop1.neighbors.add(busRoute[j])
                    stop2.neighbors.add(busRoute[i])
        toVisit: deque[int] = deque([source])
        visited: set[int] = set()
        stopCounts = 0
        while toVisit:
            roundLimit = len(toVisit)
            while roundLimit:
                curStop = toVisit.popleft()
                if curStop == target:
                    return stopCounts
                visited.add(curStop)
                for stop in graph[curStop].neighbors:
                    if stop not in visited:
                        toVisit.append(stop)
                roundLimit -= 1
            stopCounts += 1
        return -1

    def numBusesToDestination2(self, routes: list[list[int]], source: int, target: int) -> int:
        # routes: Bus# -> Stop#
        busAtStop: dict[int, list[int]] = {} # Stop# -> list[Bus#]
        for bus, stops in enumerate(routes):
            for stop in stops:
                busList = busAtStop.setdefault(stop, [])
                busList.append(bus)
        if source not in busAtStop or target not in busAtStop:
            return -1
        if source == target:
            return 0
        busCount = 0
        visitedStop: set[int] = set()
        toVisit = [source]
        while toVisit:
            nextStops: list[int] = []
            busCount += 1
            while toVisit:
                visitNow = toVisit.pop()
                busses = busAtStop[visitNow]
                for bus in busses:
                    for stop in routes[bus]:
                        if stop == target:
                            return busCount
                        if stop not in visitedStop:
                            visitedStop.add(stop)
                            nextStops.append(stop)
            toVisit = nextStops
        return -1

    def numBusesToDestination3(self, routes: list[list[int]], source: int, target: int) -> int:
        busses: dict[int, list[int]] = {} # stop -> [bus]
        for bus, stops in enumerate(routes):
            for stop in stops:
                busAtStop = busses.setdefault(stop, [])
                busAtStop.append(bus)
        toVisitStops: deque[int] = deque((source,))
        visitedStops: set[int] = set()
        takenBusses: set[int] = set()
        took = -1
        while toVisitStops:
            took += 1
            remain = len(toVisitStops)
            while remain:
                curStop = toVisitStops.popleft()
                if curStop == target: return took
                if curStop not in visitedStops:
                    visitedStops.add(curStop)
                    for bus in busses[curStop]:
                        if bus in takenBusses: continue
                        takenBusses.add(bus)
                        for stop in routes[bus]:
                            toVisitStops.append(stop)
                remain -= 1
        return -1

    def numBusesToDestination4(self, routes: list[list[int]], source: int, target: int) -> int:
        bussesAtStop: dict[int, list[int]] = {}
        for busId, stops in enumerate(routes):
            for stop in stops:
                bussesAtStop.setdefault(stop, []).append(busId)
        busCount = 0
        curStops: deque[int] = deque([source])
        visited: set[int] = set([source])
        while curStops:
            size = len(curStops)
            for _ in range(size):
                stop = curStops.popleft()
                if stop == target: return busCount
                for bus in bussesAtStop[stop]:
                    for nextStop in routes[bus]:
                        if nextStop in visited: continue
                        curStops.append(nextStop)
                        visited.add(nextStop)
                    routes[bus] = []
            busCount += 1
        return -1
                        

if __name__ == '__main__':
    routes = [[1,2,7],[3,6,7]]
    stopCount = Solution().numBusesToDestination(routes, 1, 6)
    print(stopCount)

# Mistakes:
# 1. looped in bus for stops, should use nested loop
# 2. Forgot to handle source == target case
# 3. Thought could use bus taken set instead of stop visited set, ignored the fact that multiple bus can visit one location
