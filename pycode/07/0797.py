# All Paths From Source to Target

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

# Constraints:

#     n == graph.length
#     2 <= n <= 15
#     0 <= graph[i][j] < n
#     graph[i][j] != i (i.e., there will be no self-loops).
#     All the elements of graph[i] are unique.
#     The input graph is guaranteed to be a DAG.

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res: list[list[int]] = []
        path: list[int] = [0]
        def dfs():
            if path[-1] == len(graph)-1:
                res.append(path[:])
            for n in graph[path[-1]]:
                path.append(n)
                dfs()
                path.pop()            
        dfs()
        return res

        
