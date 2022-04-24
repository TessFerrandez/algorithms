from typing import List


class Solution:
    # uses a bit extra space
    def countBits1(self, n: int) -> List[int]:
        twopow = 1

        result = [0, 1]

        while twopow < n:
            result += [i + 1 for i in result]
            twopow *= 2

        return result[:n + 1]

    def countBits2(self, n: int) -> List[int]:
        result = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            result[i] = result[i & (i - 1)] + 1
        return result

    def countBits(self, n: int) -> List[int]:
        result = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result


solution = Solution()
assert solution.countBits(2) == [0, 1, 1]
assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
