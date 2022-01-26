from collections import defaultdict
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combos = defaultdict(list)
        combos[0] = ['']

        for i in range(n + 1):
            for c in range(i):
                for left in combos[c]:
                    for right in combos[i - 1 - c]:
                        combos[i].append(f'({left}){right}')
        return combos[n]


solution = Solution()
print(solution.generateParenthesis(4))
