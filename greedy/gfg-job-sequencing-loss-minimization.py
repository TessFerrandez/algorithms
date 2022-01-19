'''
We are given N jobs numbered 1 to N. For each activity, let Ti denotes the number of days required to complete the job. For each day of delay before starting to work for job i, a loss of Li is incurred.
We are required to find a sequence to complete the jobs so that overall loss is minimized. We can only work on one job at a time.

If multiple such solutions are possible, then we are required to give the lexicographically least permutation (i.e earliest in dictionary order).

----
If all jobs took the same time to finish - pick the one with largest loss first
If all jobs had the same loss - take the one with smallest time to finish first

Now: take the one with largest Li/Ti first
But... when comparing a/b - c/d -- compare ad - bc instead
'''
from typing import List
from functools import cmp_to_key


def compare(left, right):
    if left[0][0] * right[0][1] > left[0][1] * right[0][0]:
        return -1
    else:
        return 1

def optimal_schedule(L: List[int], T: List[int]) -> List[int]:
    indices = [i + 1 for i in range(len(L))]
    pairs = list(zip(L, T))
    pairs = list(zip(pairs, indices))
    pairs = sorted(pairs, key=cmp_to_key(compare))
    return [pair[1] for pair in pairs]


assert optimal_schedule([3, 1, 2, 4], [4, 1000, 2, 5]) == [3, 4, 1, 2]
assert optimal_schedule([1, 2, 3, 5, 6], [2, 4, 1, 3, 2]) == [3, 5, 4, 1, 2]

