'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
'''
from functools import lru_cache


class Solution:
    @lru_cache()
    def numDecodings2(self, s: str) -> int:
        if len(s) == 0:
            return 1

        num_ways = 0

        if "1" <= s[0] <= "9":
            num_ways += self.numDecodings(s[1:])

        if len(s) > 1 and "1" <= s[0: 2] <= "26":
            num_ways += self.numDecodings(s[2:])

        return num_ways

    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = int(s[0] != '0')

        for i in range(2, n + 1):
            first = s[i - 1: i]
            second = s[i - 2: i]
            if '1' <= first <= '9':
                dp[i] += dp[i - 1]
            if '10' <= second <= '26':
                dp[i] += dp[i - 2]

        return dp[n]


solution = Solution()
assert solution.numDecodings("11106") == 2
assert solution.numDecodings("12") == 2
