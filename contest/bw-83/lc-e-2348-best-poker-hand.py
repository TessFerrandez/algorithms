from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
            return "Flush"

        ranks.sort()
        count = 0
        max_count = 0
        prev = -1

        for card in ranks:
            if card == prev:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
                prev = card
        max_count = max(max_count, count)

        if max_count >= 3:
            return "Three of a Kind"
        elif max_count == 2:
            return "Pair"
        else:
            return "High Card"


solution = Solution()
print(solution.bestHand([13,2,3,1,9], ["a","a","a","a","a"]))
print(solution.bestHand([4,4,2,4,4], ["d","a","a","b","c"]))
print(solution.bestHand([10,10,2,12,9], ["a","b","c","a","d"]))
print(solution.bestHand([4,3,2,10,7], ["d","a","a","b","c"]))
