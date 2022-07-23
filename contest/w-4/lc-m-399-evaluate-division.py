from collections import defaultdict, deque
from typing import List


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
assert solution.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]) == [6.0, 0.5, -1.0, 1.0, -1.0]
assert solution.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]) == [3.75000,0.40000,5.00000,0.20000]
assert solution.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]) == [0.50000,2.00000,-1.00000,-1.00000]
