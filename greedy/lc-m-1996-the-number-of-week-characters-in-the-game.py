from collections import defaultdict
from typing import List


class Solution:
    def numberOfWeakCharacters1(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        weak = 0
        current_max = 0

        for _, defense in properties:
            if defense < current_max:
                weak += 1
            else:
                current_max = defense
        return weak

    def numberOfWeakCharacters2(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))

        weak = 0
        stack = []

        for _, defense in properties:
            if stack and stack[-1] < defense:
                stack.pop()
                weak += 1
            stack.append(defense)

        return weak

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        weak, max_d = 0, -1
        defense = defaultdict(list)

        for a, d in properties:
            defense[a].append(d)

        for attack in sorted(list(defense.keys()))[::-1]:
            for d in defense[attack]:
                if d < max_d:
                    weak += 1
            for d in defense[attack]:
                max_d = max(max_d, d)

        return weak


solution = Solution()
assert solution.numberOfWeakCharacters([[6, 9], [7, 5], [7, 9], [7, 10], [10, 4], [10, 7]]) == 2
assert solution.numberOfWeakCharacters([[5, 5], [6, 3], [3, 6]]) == 0
assert solution.numberOfWeakCharacters([[5, 5], [6, 6], [6, 3], [3, 6]]) == 1
assert solution.numberOfWeakCharacters([[2, 2], [3, 3]]) == 1
