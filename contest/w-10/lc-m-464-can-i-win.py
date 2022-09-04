class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def can_win(choices, remainder):
            # we can win directly choosing the highest
            if choices[-1] >= remainder:
                return True

            # we have seen this scenario before
            scenario = tuple(choices)
            if scenario in seen:
                return seen[scenario]

            # pick a choice and let the other player go
            # if the other player looses we can force a win
            for i in range(len(choices)):
                if not can_win(choices[:i] + choices[i + 1:], remainder - choices[i]):
                    seen[scenario] = True
                    return True

            # got here and we have a loss => this is a loose loose situation
            seen[scenario] = False
            return False

        choices = list(range(1, maxChoosableInteger + 1))
        choice_sum = sum(choices)

        if choice_sum < desiredTotal:
            return False                    # no one can win
        if choice_sum == desiredTotal:
            return maxChoosableInteger % 2  # I win if there are an odd number of choices

        seen = {}
        return can_win(choices, desiredTotal)


solution = Solution()
assert not solution.canIWin(10, 11)
assert solution.canIWin(10, 0)
assert solution.canIWin(10, 1)
