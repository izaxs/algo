class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph: dict[int, list[int]] = {}
        indegree: list[int] = [0]*numCourses
        for pair in prerequisites:
            graph.setdefault(pair[1], []).append(pair[0])
            indegree[pair[0]] += 1
        courseTakenOrder: list[int] = []
        toTake = [i for i, v in enumerate(indegree) if v == 0]
        for c in toTake:
            courseTakenOrder.append(c)
            for nextCourse in graph.get(c, []):
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    toTake.append(nextCourse)
        if (len(courseTakenOrder) != numCourses): return []
        return courseTakenOrder