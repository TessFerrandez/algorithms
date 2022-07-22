from bisect import bisect_left, bisect_right
from math import inf
from operator import itemgetter


# TLE
class CountIntervals1:
    def __init__(self):
        self.intervals = []
        self.counts = []

    def add(self, left: int, right: int) -> None:
        # add the interval
        i = bisect_left(self.intervals, [left, right])
        if i != 0 and self.intervals[i - 1][1] >= left:
            self.intervals[i - 1][1] = max(self.intervals[i - 1][1], right)
            self.counts[i - 1] = self.intervals[i - 1][1] - self.intervals[i - 1][0] + 1
            i = i - 1
        else:
            self.intervals.insert(i, [left, right])
            self.counts.insert(i, right - left + 1)

        # merge intervals
        while i + 1 < len(self.intervals) and self.intervals[i][1] >= self.intervals[i + 1][0]:
            self.intervals[i][1] = max(self.intervals[i][1], self.intervals[i + 1][1])
            del self.intervals[i + 1]
            del self.counts[i + 1]
            self.counts[i] = self.intervals[i][1] - self.intervals[i][0] + 1

    def count(self) -> int:
        return sum(self.counts)


class CountIntervals:
    def __init__(self):
        self.intervals = [(-inf, -inf), (inf, inf)]
        self.coverage = 0

    def add(self, left: int, right: int) -> None:
        intervals = self.intervals

        left_index = bisect_left(intervals, left - 1, key=itemgetter(1))
        left_val = min(intervals[left_index][0], left)

        right_index = bisect_right(intervals, right + 1, key=itemgetter(0))
        right_val = max(intervals[right_index - 1][1], right)

        to_delete = 0
        for _ in range(left_index, right_index):
            to_delete += intervals[_][1] - intervals[_][0] + 1

        self.coverage += right_val - left_val + 1 - to_delete
        intervals[left_index: right_index] = [[left_val, right_val]]

    def count(self) -> int:
        return self.coverage


ci = CountIntervals()
ci.add(5, 10)
ci.add(3, 5)
assert ci.count() == 8

ci = CountIntervals()
ci.add(2, 3)
ci.add(7, 10)
assert ci.count() == 6
ci.add(5, 8)
assert ci.count() == 8

ci = CountIntervals()
assert ci.count() == 0
ci.add(8, 43)
ci.add(13, 16)
ci.add(26, 33)
ci.add(28, 36)
ci.add(29, 37)
assert ci.count() == 36
ci.add(34, 46)
ci.add(10, 23)
