from math import inf


def find_substring(s: str) -> str:
    valid = False
    start, end = 0, 0   # start and end of substring
    shortest = inf

    while end < len(s):
        # expand end until window is valid
        while not valid:
            end += 1

        # shrink start until window is not valid
        while valid:
            start += 1

        # record shortest substring

    return shortest
