from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        count = 0
        while trainers and players:
            while players and players[-1] > trainers[-1]:
                players.pop()
            if players:
                players.pop()
                trainers.pop()
                count += 1

        return count


solution = Solution()
assert solution.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]) == 2
assert solution.matchPlayersAndTrainers([1, 1, 1, 1], [10]) == 1
