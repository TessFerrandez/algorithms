from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key, value, timestamp):
        self.lookup[key].append([timestamp, value])

    def get(self, key, timestamp):
        values = self.lookup[key]
        low, high = 0, len(self.lookup[key])

        while low < high:
            mid = (low + high) // 2
            if values[mid][0] <= timestamp:
                low = mid + 1
            else:
                high = mid

        return '' if high == 0 else values[high - 1][1]


tm = TimeMap()
tm.set("foo", "bar", 1)
assert tm.get("foo", 1) == "bar"
assert tm.get("foo", 3) == "bar"
tm.set("foo", "bar2", 4)
assert tm.get("foo", 4) == "bar2"
assert tm.get("foo", 5) == "bar2"
