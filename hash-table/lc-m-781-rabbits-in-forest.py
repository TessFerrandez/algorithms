from collections import Counter
from math import ceil
from typing import List


class Solution:
    def numRabbits1(self, answers: List[int]) -> int:
        count_answers = Counter(answers)

        total_rabbits = 0

        for answer, freq in count_answers.items():
            rabbits_in_group = answer + 1
            groups = ceil(freq / rabbits_in_group)
            total_rabbits += groups * rabbits_in_group

        return total_rabbits

    # annoyingly short - bc ceil((n + x) / (x + 1)) = (n + x) // (x + 1)
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        return sum((freq[answer] + answer) // (answer + 1) * (answer + 1) for answer in freq)


solution = Solution()
assert solution.numRabbits([1, 1, 2]) == 5
assert solution.numRabbits([10, 10, 10]) == 11
