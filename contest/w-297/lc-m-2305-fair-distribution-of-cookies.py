from cmath import inf
from functools import cache
from typing import List


class Solution:
    # backtracking
    def distributeCookies1(self, cookies: List[int], k: int) -> int:
        answer = float('inf')
        fair = [0] * k

        def rec(i):
            nonlocal answer, fair
            if i == len(cookies):
                answer = min(answer, max(fair))
                return
            # bounding condition to stop branch
            # if unfairness already exceeds current optimal solution
            if answer <= max(fair):
                return
            for j in range(k):
                fair[j] += cookies[i]
                rec(i + 1)
                fair[j] -= cookies[i]

        rec(0)
        return answer

    # masked dp
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)

        @cache
        def dp(mask, k):
            # return min unfairness of distributing cookies marked by mask to k children
            if mask == 0:
                return 0
            if k == 0:
                return inf
            answer = inf
            original = mask
            while mask:
                mask = original & (mask - 1)
                amount = sum(cookies[i] for i in range(n) if (original ^ mask) & 1 << i)
                answer = min(answer, max(amount, dp(mask, k - 1)))
            return answer

        return dp((1 << n) - 1, k)


solution = Solution()
print(solution.distributeCookies([8, 15, 10, 20, 8], 2))
print(solution.distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3))
