from __future__ import annotations
from typing import Optional
import heapq

class Node:
    def __init__(self, num: int) -> None:
        self.id = num
        self.dists: dict[int, int] = {} # key: id, value: dist

class Path:
    def __init__(self, start: int = -1, other: Optional[Path] = None) -> None:
        if other:
            self.dist = other.dist
            self.path = other.path[:]
        else:
            self.dist = 0
            self.path: list[int] = [start]

    def __lt__(self, other: Path) -> bool:
        if self.dist != other.dist: return self.dist < other.dist
        if len(self.path) != len(other.path): return len(self.path) < len(other.path)
        return self.path[-1] < other.path[-1]

    def __repr__(self) -> str:
        return f'dist: {self.dist}, path: {self.path}'

def build_graph(edges: list[tuple[int, int, int]]) -> dict[int, Node]:
    graph: dict[int, Node] = {}
    for i1, i2, dist in edges:
        n1 = graph.setdefault(i1, Node(i1))
        n2 = graph.setdefault(i2, Node(i2))
        preDist = n1.dists.setdefault(i2, dist)
        dist = min(dist, preDist)
        n1.dists[i2], n2.dists[i1] = dist, dist
    return graph

def find_shortest(edges: list[tuple[int, int, int]], start: int, end: int) -> Path:
    graph = build_graph(edges)
    if start not in graph or end not in graph: return Path()
    visited: set[int] = set()
    nextVisits: list[Path] = [Path(start)] # list of path
    while nextVisits:
        curPath = heapq.heappop(nextVisits)
        curId = curPath.path[-1]
        visited.add(curId)
        if curId == end: return curPath
        for nextId, nextDist in graph[curId].dists.items():
            if nextId in visited: continue
            nextPath = Path(other=curPath)
            nextPath.path.append(nextId)
            nextPath.dist += nextDist
            heapq.heappush(nextVisits, nextPath)
    return Path()

edges = [(0, 1, 4), (0, 2, 7), (1, 2, 2), (2, 3, 3), (1, 3, 8), (2, 4, 1), (4, 3, 1)]
print(find_shortest(edges, 0, 3))
