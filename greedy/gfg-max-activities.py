'''
Given a set of start times (s) and finish times (f)
sorted by earliest finish time, what is the maximum set of
activities that one single person can do?

ex:
start   10  12  20
finish  20  15  30

Result [0, 2] 10->20 + 20->30

ex.
start   1   3   0   5   8   5
finish  2   4   6   7   9   9

Result [0, 1, 3, 4]
'''

from typing import List


def printMaxActivities(s: List[int], f: List[int]) -> List[int]:
    activities = [0]
    prev_finish = f[0]

    for i in range(1, len(s)):
        if s[i] >= prev_finish:
            activities.append(i)
            prev_finish = f[i]

    return activities


assert printMaxActivities([10, 12, 20], [20, 15, 30]) == [0, 2]
assert printMaxActivities([1, 2, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]) == [0, 1, 3, 4]
