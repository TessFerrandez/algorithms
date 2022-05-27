from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        dp = []

        for _, height in envelopes:
            left = bisect_left(dp, height)
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height

        return len(dp)

    # TLE
    def maxEnvelopes1(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        envelopes.sort()
        n = len(envelopes)
        dp = [0] * n

        result = 0
        for i in range(n):
            dp[i] = 1

            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], 1 + dp[j])

            result = max(result, dp[i])
        return result

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        Same as 300 increasing sub sequences
        for [1, 3], [3, 5], [6, 8], [6, 7], [8, 4], [9, 5]
        we work with [3, 5, 8, 7, 4, 5] and find the longest increasing subsequence
        '''
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        dp = [10 ** 10] * (len(envelopes) + 1)
        for envelope in envelopes:
            dp[bisect_left(dp, envelope[1])] = envelope[1]
        return dp.index(10 ** 10)


solution = Solution()
assert solution.maxEnvelopes([[1, 3], [3, 5], [6, 8], [6, 7], [8, 4], [9, 5]]) == 3
assert solution.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3
assert solution.maxEnvelopes([[1,1],[1,1],[1,1]]) == 1
