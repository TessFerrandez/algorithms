from functools import cmp_to_key
from typing import List


class Solution:
    # iterative
    def lexicalOrder1(self, n: int) -> List[int]:
        results = [1]
        while len(results) < n:
            num = results[-1] * 10
            while num > n:
                num //= 10
                num += 1
                while num % 10 == 0:
                    num //= 10
            results.append(num)
        return results

    # using sorting
    def lexicalOrder2(self, n: int) -> List[int]:
        highest = 1

        while highest * 10 <= n:
            highest *= 10

        def mycmp(a, b, highest=highest):
            while a < highest:
                a *= 10
            while b < highest:
                b *= 10
            return -1 if a < b else b < a

        return sorted(range(1, n + 1), key=cmp_to_key(mycmp))

    # using sorting
    def lexicalOrder3(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=lambda x: str(x))

    # recursive
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(current):
            if current > n:
                return

            result.append(current)
            for i in range(0, 10):
                if 10 * current + i > n:
                    return
                dfs(10 * current + i)

        for i in range(1, 10):
            dfs(i)

        return result


solution = Solution()
assert solution.lexicalOrder(13) == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
assert solution.lexicalOrder(2) == [1, 2]
