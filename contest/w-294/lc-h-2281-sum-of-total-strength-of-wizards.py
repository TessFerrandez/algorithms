from itertools import accumulate
from typing import List


class Solution:
    # TLE
    def totalStrength1(self, strength: List[int]) -> int:
        sums = [0]
        prev = 0
        for s in strength:
            prev = prev + s
            sums.append(prev)

        total = 0
        for left in range(len(strength)):
            lowest = strength[left]
            for right in range(left, len(strength)):
                lowest = min(lowest, strength[right])
                total += lowest * (sums[right + 1] - sums[left])

        return total % (10 ** 9 + 7)

    def totalStrength(self, strength: List[int]) -> int:
        mod = (10 ** 9 + 7)
        n = len(strength)

        # next small on the right
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                right[stack.pop()] = i
            stack.append(i)

        # next small on the left
        left = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                left[stack.pop()] = i
            stack.append(i)

        # for each strength[i] as minimum, calculate sum
        result = 0
        sums = list(accumulate(accumulate(strength), initial=0))
        for i in range(n):
            l, r = left[i], right[i]
            l_sum = sums[i] - sums[max(l, 0)]
            r_sum = sums[r] - sums[i]
            l_n, r_n = i - l, r - i
            result += strength[i] * (r_sum * l_n - l_sum * r_n) % mod
        return result % mod


solution = Solution()
# 44
print(solution.totalStrength([1, 3, 1, 2]))
# 47
print(solution.totalStrength([1, 1, 2, 3]))
# 213
print(solution.totalStrength([5, 4, 6]))
# 471441678
print(solution.totalStrength([747,812,112,1230,1426,1477,1388,976,849,1431,1885,1845,1070,1980,280,1075,232,1330,1868,1696,1361,1822,524,1899,1904,538,731,985,279,1608,1558,930,1232,1497,875,1850,1173,805,1720,33,233,330,1429,1688,281,362,1963,927,1688,256,1594,1823,743,553,1633,1898,1101,1278,717,522,1926,1451,119,1283,1016,194,780,1436,1233,710,1608,523,874,1779,1822,134,1984]))
