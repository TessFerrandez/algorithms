from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        pickups = {}
        best = float('inf')

        for i, card in enumerate(cards):
            if card in pickups:
                best = min(i - pickups[card] + 1, best)
            pickups[card] = i

        return -1 if best == float('inf') else best


solution = Solution()
assert solution.minimumCardPickup([3,4,2,3,4,7]) == 4
assert solution.minimumCardPickup([1,0,5,3]) == -1
