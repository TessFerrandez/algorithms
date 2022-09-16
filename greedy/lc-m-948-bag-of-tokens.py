from collections import deque
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        tokens = deque(tokens)

        best_score = 0
        score = 0
        while tokens and (score > 0 or power >= tokens[0]):
            if power >= tokens[0]:
                power -= tokens.popleft()
                score += 1
            else:
                power += tokens.pop()
                score -= 1
            best_score = max(score, best_score)
        return best_score


solution = Solution()
assert solution.bagOfTokensScore([100], 50) == 0
assert solution.bagOfTokensScore([100, 200], 150) == 1
assert solution.bagOfTokensScore([100, 200, 300, 400], 200) == 2
