class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
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
        curStops = [source]
        while curStops:
            nextStops: list[int] = []
            busCount += 1
            while curStops:
                visitNow = curStops.pop()
                busses = busAtStop[visitNow]
                for bus in busses:
                    for stop in routes[bus]:
                        if stop == target:
                            return busCount
                        if stop not in visitedStop:
                            visitedStop.add(stop)
                            nextStops.append(stop)
            curStops = nextStops
        return -1

# Mistakes:
# 1. looped in bus for stops, should use nested loop
# 2. Forgot to handle source == target case
# 3. Thought could use bus taken set instead of stop visited set, ignored the fact that multiple bus can visit one location
