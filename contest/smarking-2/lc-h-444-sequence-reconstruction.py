from math import inf
from typing import List


class Solution:
    def sequenceReconstruction1(self, org: List[int], seqs: List[List[int]]) -> bool:
        n = len(org)

        # possible positions for the given number
        min_pos, max_pos = [0] * n, [n - 1] * n

        original_positions = {org[i]: i for i in range(n)}
        original_positions[inf] = n

        checked = False

        for sequence in seqs:
            for first, second in zip(sequence, sequence[1:] + [inf]):
                if first not in original_positions or second not in original_positions:
                    return False
                first_pos = original_positions[first]
                second_pos = original_positions[second]
                max_pos[first_pos] = min(max_pos[first_pos], second_pos - 1)
                if second_pos < n:
                    min_pos[second_pos] = max(min_pos[second_pos], first_pos + 1)

        if n == 1 and checked:
            return False
        for i in range(n):
            if max_pos[i] != min_pos[i]:
                return False
        return True

    def sequenceReconstruction2(self, org: List[int], seqs: List[List[int]]) -> bool:
        pre = {}
        index = {org[i]: i for i in range(len(org))}

        for sequence in seqs:
            for i, number in enumerate(sequence):
                if number not in index:
                    return False

                if number not in pre:
                    pre[number] = index[sequence[i - 1]] if i > 0 else -1
                else:
                    pre[number] = max(pre[number], index[sequence[i - 1]] if i > 0 else -1)

        for i, number in enumerate(org):
            if number not in pre or pre[number] != i - 1:
                return False

        return True

    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        n = len(org)
        index = {org[i]: i for i in range(n)}
        checked = [False] * n
        has_checked = False
        to_check = n - 1

        for sequence in seqs:
            for i, current in enumerate(sequence):
                has_checked = True

                if current <= 0 or current > n:
                    return False

                if i == 0:
                    continue

                previous = sequence[i - 1]
                if index[previous] >= index[current]:
                    return False

                if not checked[index[current]] and index[previous] == index[current] - 1:
                    checked[index[current]] = True
                    to_check -= 1

        return to_check == 0 and has_checked


solution = Solution()
assert not solution.sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3]])
assert not solution.sequenceReconstruction([1, 2, 3], [[1, 2]])
assert solution.sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3], [2, 3]])
assert solution.sequenceReconstruction([4, 1, 5, 2, 6, 3], [[5, 2, 6, 3], [4, 1, 5, 2]])
