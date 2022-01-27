'''
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.
'''
from typing import List
from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def get_chain(lookup, a, b):
            todo = deque([(a, 1)])
            visited = set([a])

            if a == b:
                return 1

            while todo:
                current, product = todo.popleft()

                for neighbor in lookup[current]:
                    if neighbor == b:
                        return product * lookup[current][neighbor]

                    if neighbor not in visited:
                        visited.add(neighbor)
                        todo.append((neighbor, product * lookup[current][neighbor]))

            return -1.0

        lookup = defaultdict(dict)

        for i, equation in enumerate(equations):
            a, b = equation
            result = values[i]
            lookup[a][a] = 1.0
            lookup[a][b] = result
            lookup[b][b] = 1.0
            lookup[b][a] = 1 / result

        lookup = dict(lookup)

        answer = []
        for a, b in queries:
            if a not in lookup or b not in lookup:
                answer.append(-1.0)
            elif b in lookup[a]:
                answer.append(lookup[a][b])
            else:
                answer.append(get_chain(lookup, a, b))
        return answer


solution = Solution()
print(solution.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
print(solution.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))
