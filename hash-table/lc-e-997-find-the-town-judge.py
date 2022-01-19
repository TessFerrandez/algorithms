'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
'''
from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(int)
        trusted = defaultdict(int)

        for ai, bi in trust:
            trusts[ai] += 1
            trusted[bi] += 1

        for i in range(1, n + 1):
            if trusts[i] == 0 and trusted[i] == n - 1:
                return i

        return -1


solution = Solution()
assert solution.findJudge(2, [[1,2]]) == 2
assert solution.findJudge(3, [[1,3],[2,3]]) == 3
assert solution.findJudge(3, [[1,3],[2,3],[3,1]]) == -1
