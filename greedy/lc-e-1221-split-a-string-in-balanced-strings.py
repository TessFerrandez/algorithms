'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.
'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        num_strings = 0

        for ch in s:
            if ch == 'R':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                num_strings += 1

        return num_strings


solution = Solution()
assert solution.balancedStringSplit('RLRRLLRLRL') == 4
assert solution.balancedStringSplit('RLLLLRRRLR') == 3
assert solution.balancedStringSplit('LLLLRRRR') == 1
