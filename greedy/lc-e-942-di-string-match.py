'''
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
'''
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n

        answer = []
        for ch in s:
            if ch == 'I':
                answer.append(low)
                low += 1
            else:
                answer.append(high)
                high -= 1

        answer.append(low)
        return answer


solution = Solution()
assert solution.diStringMatch('IDID') == [0, 4, 1, 3, 2]
assert solution.diStringMatch('III') == [0, 1, 2, 3]
assert solution.diStringMatch('DDI') == [3, 2, 0, 1]
