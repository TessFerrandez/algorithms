from functools import cache
from math import comb


def non_bouncy(total_length):
    @cache
    def increasing(length, starts_with):
        if length == 1:
            return 1

        result = 0

        for i in range(starts_with, 10):
            result += increasing(length - 1, i)

        return result

    @cache
    def decreasing(length, starts_with):
        if length == 1 or starts_with == 0:
            return 1

        result = 0

        for i in range(starts_with, -1, -1):
            result += decreasing(length - 1, i)

        return result

    count_increasing = 0
    count_decreasing = 0

    for length in range(1, total_length + 1):
        for starts_with in range(1, 10):
            count_increasing += increasing(length, starts_with)
            count_decreasing += decreasing(length, starts_with)

    duplicates = 9 * total_length                                   # 11 22 33 .. 111 222 333 ..
    total_sum = count_increasing + count_decreasing - duplicates
    return total_sum


def non_bouncy2(total_length):
    result = comb(total_length + 9, 9) + comb(total_length + 10, 10) - 10 * total_length - 2
    return result


assert non_bouncy(6) == 12951
assert non_bouncy(100) == 51161058134250

assert non_bouncy2(6) == 12951
assert non_bouncy2(100) == 51161058134250
