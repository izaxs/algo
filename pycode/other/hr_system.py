CODE_OK = 0
CODE_ERROR = 1

class Position:
    def __init__(self, position: str, salaryRate: int, startDate: int):
        self.position = position
        self.salaryRate = salaryRate
        self.startDate = startDate

class Worker:
    def __init__(self, name, position: str, salaryRate: int):
        self.name = name
        self.positions = [Position(position, salaryRate, 0)]

    def getPosition(self, curDate: int = -1) -> Position:
        if curDate >= 0:
            for p in reversed(self.positions):
                if p.startDate <= curDate:
                    return p
        return self.positions[-1]
    
    def promote(self, position: str, salaryRate: int, startDate: int) -> int:
        newPositions: list[Position] = []
        for p in self.positions:
            if p.startDate < startDate:
                newPositions.append(p)
            else:
                break
        self.positions = newPositions
        self.positions.append(Position(position, salaryRate, startDate))
        return CODE_OK

# hour range[0, 23]     
class Session:
    IMCOMPLETE = -1
    HOURS_PER_DAY = 24

    def __init__(self, worker: Worker, startDate: int, startHour: int):
        self.position = worker.getPosition(startDate)
        self.startDate = startDate
        self.startHour = startHour
        self.endDate = self.IMCOMPLETE
        self.endHour = self.IMCOMPLETE

    def isCompleted(self) -> bool:
        return not (self.endDate == self.IMCOMPLETE or self.endHour == self.IMCOMPLETE)

    def getDurationHour(self) -> int:
        if not self.isCompleted(): return 0
        return (self.endHour - self.startHour) + (self.endDate - self.startDate) * self.HOURS_PER_DAY
    
    def inDateRange(self, startDate: int, endDate: int) -> int:
        return self.startDate >= startDate and self.endDate <= endDate 
    
    def getSalary(self) -> int:
        if not self.isCompleted(): return 0
        return self.getDurationHour() * self.position.salaryRate

    def getSalaryByRange(self, startDate: int, endDate: int) -> int:
        if not self.isCompleted(): return 0
        startHour = self.startHour if startDate <= self.startDate else 0
        startDate = max(startDate, self.startDate)
        endHour = self.endHour if endDate >= self.endDate else self.HOURS_PER_DAY - 1
        salary = ((endHour - startHour) + (self.endDate - self.startDate) * self.HOURS_PER_DAY) * self.position.salaryRate
        return max(salary, 0)
        

class HR:
    def __init__(self):
        self.workers: dict[str, Worker] = {}
        self.sessionRecorder: dict[str, list[Session]] = {} # workerName -> list(session)

    def addWorker(self, name: str, position: str, salaryRate: int) -> int:
        if name in self.workers: return CODE_OK
        self.workers[name] = Worker(name, position, salaryRate)
        return CODE_OK
    
    def registerEnter(self, name: str, startDate: int, startHour: int) -> int:
        if name not in self.workers: return CODE_ERROR
        sessions = self.sessionRecorder.setdefault(name, [])
        if sessions and not sessions[-1].isCompleted(): return CODE_ERROR
        curSession = Session(self.workers[name], startDate, startHour)
        sessions.append(curSession)
        return CODE_OK
    
    def registerExit(self, name: str, endDate: int, endHour: int) -> int:
        if name not in self.workers: return CODE_ERROR
        sessions = self.sessionRecorder.setdefault(name, [])
        if not sessions or sessions[-1].isCompleted(): return CODE_ERROR
        curSession = sessions[-1]
        if endDate < curSession.startDate or endHour < curSession.startHour:
            return CODE_ERROR
        curSession.endDate = endDate
        curSession.endHour = endHour
        return CODE_OK
    
    def getTotalDuration(self, name: str) -> int:
        if name not in self.workers: return 0
        workerSessions = self.sessionRecorder.setdefault(name, [])
        totalDuration = 0
        for session in workerSessions:
            totalDuration += session.getDurationHour()
        return totalDuration
    
    def getTopNTime(self, position: str, topN: int) -> list[str]:
        workersTime: list[tuple[str, int]] = [] # name, time
        for worker in self.workers.keys():
            workerSessions = self.sessionRecorder.setdefault(worker, [])
            workerTime = 0
            for session in workerSessions:
                workerTime += session.getDurationHour()
            workersTime.append((worker, workerTime))
        workersTime.sort(key=lambda x: -x[1])
        workers = [worker[0] for worker in workersTime[:topN]]
        return workers
                    
        

    def promote(self, name: str, position: str, salaryRate: int, startDate: int) -> int:
        if name not in self.workers: return CODE_ERROR
        worker = self.workers[name]
        return worker.promote(position, salaryRate, startDate)
    
    def getSalary(self, name: str, startDate: int, endDate: int) -> int:
        if name not in self.workers: return 0
        workerSessions = self.sessionRecorder.setdefault(name, [])
        salary = 0
        for session in workerSessions:
            if not session.isCompleted() or not session.inDateRange(startDate, endDate): continue
            salary += session.getSalary()
        return salary

