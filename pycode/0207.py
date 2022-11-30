class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegrees: list[int] = [0]*numCourses
        children: dict[int, list[int]] = {}
        for p in prerequisites:
            indegrees[p[0]] += 1
            children.setdefault(p[1], []).append(p[0])
        courseTaken: set[int] = set()

        def bfs():
            nonlocal indegrees, courseTaken
            courseToTake: list[int] = []
            nextIndegrees = list(indegrees)
            for course, indegree in enumerate(indegrees):
                if indegree == 0 and course not in courseTaken:
                    courseToTake.append(course)
                    courseTaken.add(course)
                    nextIndegrees[course] = -1
            if not courseToTake:
                return
            for course in courseToTake:
                childCourses = children.get(course, [])
                for childCourse in childCourses:
                    nextIndegrees[childCourse] -= 1
            indegrees = nextIndegrees
            bfs()
        bfs()
        return len(courseTaken) == numCourses


        