from __future__ import annotations
from heapq import heappush, heappop

class Task:
    def __init__(self, index: int, start: int, lasts: int) -> None:
        self.index = index
        self.start = start
        self.lasts = lasts

    def __lt__(self, other: Task) -> bool:
        return self.lasts < other.lasts

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        taskList = [Task(index, val[0], val[1]) for index, val in enumerate(tasks)]
        taskList.sort(key=lambda x: (x.start, x.lasts, x.index))
        i, curTime = 0, 0
        res: list[int] = []
        todos: list[Task] = []
        while todos or i < len(taskList):
            while i < len(taskList) and taskList[i].start <= curTime:
                heappush(todos, taskList[i])
                i += 1
            if todos:
                nextTask = heappop(todos)
                res.append(nextTask.index)
                curTime = curTime+nextTask.lasts
            elif i < len(taskList):
                curTime = taskList[i].start
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getOrder([[1,2],[2,4],[3,2],[4,1]]))