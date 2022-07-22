from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)

        players = set()
        for winner, looser in matches:
            players.add(winner)
            players.add(looser)
            losses[looser] -= 1

        players = sorted(players)

        zero, one = [], []
        for player in players:
            if losses[player] == 0:
                zero.append(player)
            if losses[player] == -1:
                one.append(player)

        return [zero, one]


solution = Solution()
assert solution.findWinners([[1, 100000]]) == [[1], [100000]]
assert solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]) == [[1, 2, 10], [4, 5, 7, 8]]
assert solution.findWinners([[2,3],[1,3],[5,4],[6,4]]) == [[1, 2, 5, 6], []]
