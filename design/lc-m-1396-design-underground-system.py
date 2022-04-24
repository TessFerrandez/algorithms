from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.checkins = {}
        self.averages = defaultdict(lambda: (0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        from_stn, from_time = self.checkins[id]
        trip_time = t - from_time
        avg_time, trips = self.averages[(from_stn, stationName)]
        total_time = (avg_time * trips) + trip_time
        self.averages[(from_stn, stationName)] = (total_time / (trips + 1), trips + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        avg_time, _ = self.averages[(startStation, endStation)]
        return avg_time


underground = UndergroundSystem()
underground.checkIn(45, "Leyton", 3)
underground.checkIn(32, "Paradise", 8)
underground.checkIn(27, "Leyton", 10)
underground.checkOut(45, "Waterloo", 15)
underground.checkOut(27, "Waterloo", 20)
underground.checkOut(32, "Cambridge", 22)
assert underground.getAverageTime("Paradise", "Cambridge") == 14
assert underground.getAverageTime("Leyton", "Waterloo") == 11
underground.checkIn(10, "Leyton", 24)
assert underground.getAverageTime("Leyton", "Waterloo") == 11
underground.checkOut(10, "Waterloo", 38)
assert underground.getAverageTime("Leyton", "Waterloo") == 12

underground = UndergroundSystem()
underground.checkIn(10, "Leyton", 3)
underground.checkOut(10, "Paradise", 8)
assert underground.getAverageTime("Leyton", "Paradise") == 5
underground.checkIn(5, "Leyton", 10)
underground.checkOut(5, "Paradise", 16)
assert underground.getAverageTime("Leyton", "Paradise") == 5.5
underground.checkIn(2, "Leyton", 21)
underground.checkOut(2, "Paradise", 30)
assert underground.getAverageTime("Leyton", "Paradise") == 20 / 3
