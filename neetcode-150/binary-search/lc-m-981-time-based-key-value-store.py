from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookup[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.lookup[key]
        left, right = 0, len(values)

        while left < right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return '' if right == 0 else values[right - 1][1]


tm = TimeMap()
tm.set('foo', 'bar', 1)
assert tm.get('foo', 1) == 'bar'
assert tm.get('foo', 3) == 'bar'
tm.set('foo', 'bar2', 4)
assert tm.get('foo', 4) == 'bar2'
assert tm.get('foo', 5) == 'bar2'
