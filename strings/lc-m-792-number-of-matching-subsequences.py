from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])


solution = Solution()
assert solution.numMatchingSubseq("abcde", ["a","bb","acd","ace"]) == 3
assert solution.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]) == 2
