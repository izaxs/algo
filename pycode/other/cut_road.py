# N cities (from 1 to N) are connected by M roads (for example, 1 <-> 2, roads are bidirectional).
# You want to maintain as less roads as possible but to keep the same accessibility (if you had path from i to j you need to keep them connected)
# Find which roads can be deleted. If there are multiple solutions return any of them.
# Example:
# num_cities=3, roads=[(1,2), (2,3), (3,1)] -> [(3, 1)] (road from 3 to 1 can be deleted)
# 1 - 2  ->. 1-2
# | /.        /
# 3          3

# graph1: key: city -> value: [directly connected] :   1: [2,3]    2: [1,3]     3:[1,2]
# hasset: connected pairs: start from most connected city in graph: dfs, put all connection in hashset
# road: 1 -> 2,3  (1,2) (1,3)
# reducedCon = (1,2) (1,3)
# 2 -> 1,3 output: (2,3)
# 1-2
# |/
# 3-4
# Order: 3,2,1,4
# reduced: (1,3), (1,2)
# visited: (1,3), (2,3), (1,2)

def buildGraph(roads: list[tuple[int, int]]) -> dict[int, list[int]]:
    res: dict[int, list[int]] = {}
    for a, b in roads:
        aNb = res.setdefault(a, [])
        aNb.append(b)
        bNb = res.setdefault(b, [])
        bNb.append(a)
    return res

def minify(graph: dict[int, list[int]], newRoads: list[tuple[int, int]]):
    visited: set[int] = set()
    toVisit: list[int] = [k for k in graph]
    toVisit.sort(key=lambda x: -len(graph[x]))
    for city in toVisit:
        visited.add(city)
        for nb in graph[city]:
            if nb in visited: continue
            newRoads.append((city, nb))
            visited.add(nb)

def trim(oldRoad: list[tuple[int, int]], newRoad: list[tuple[int, int]]) -> list[tuple[int, int]]:
    trimmed = set(oldRoad)
    for a, b in newRoad:
        trimmed.discard((a, b))
        trimmed.discard((b, a))
    return list(trimmed)

def reduceRoad(roads: list[tuple[int, int]]) -> list[tuple[int, int]]:
    graph = buildGraph(roads)
    newRoads: list[tuple[int, int]] = []
    minify(graph, newRoads)
    return trim(roads, newRoads)


# roads = [(1,2), (2,3), (3,1)]
# roads = [(1,2), (2,3), (3,1), (3, 4), (2, 4)]
roads = [(1,2), (2,3), (3,4), (4,5), (5, 6)]
roads = [(1,2), (2,3), (3,4), (4,5), (5, 6), (2,7), (7,5)]
roads = [(1,2),(1,3),(1,4),(1,5),(2,3),(3,5),(4,5),(2,4)]
roads = [(1,2),(1,3),(1,4),(1,5),(2,3),(3,5),(4,5),(2,4), (6,7),(6,8),(6,9),(8,9)]
res = reduceRoad(roads)
print(res)