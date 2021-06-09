class UndergroundSystem:

    def __init__(self):
        self.time = {} # {(startStation, endStation) : (averageTime, count)}
        self.trip = {} # {id : (startStation, startTime)}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trip[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkInTime = self.trip[id]
        timeUsed = t - checkInTime
        averageTime, count = self.time.get((startStation, stationName), (0, 0))
        averageTime = (averageTime * count + timeUsed) / (count + 1)
        self.time[(startStation, stationName)] = (averageTime, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        averageTime, _ = self.time.get((startStation, endStation), (0, 0))
        return averageTime