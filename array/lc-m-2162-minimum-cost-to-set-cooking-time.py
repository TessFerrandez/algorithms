'''
A generic microwave supports cooking times for:

at least 1 second.
at most 99 minutes and 99 seconds.
To set the cooking time, you push at most four digits. The microwave normalizes what you push as four digits by prepending zeroes. It interprets the first two digits as the minutes and the last two digits as the seconds. It then adds them up as the cooking time. For example,

You push 9 5 4 (three digits). It is normalized as 0954 and interpreted as 9 minutes and 54 seconds.
You push 0 0 0 8 (four digits). It is interpreted as 0 minutes and 8 seconds.
You push 8 0 9 0. It is interpreted as 80 minutes and 90 seconds.
You push 8 1 3 0. It is interpreted as 81 minutes and 30 seconds.
You are given integers startAt, moveCost, pushCost, and targetSeconds. Initially, your finger is on the digit startAt. Moving the finger above any specific digit costs moveCost units of fatigue. Pushing the digit below the finger once costs pushCost units of fatigue.

There can be multiple ways to set the microwave to cook for targetSeconds seconds but you are interested in the way with the minimum cost.

Return the minimum cost to set targetSeconds seconds of cooking time.

Remember that one minute consists of 60 seconds.
'''
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def get_cost(minutes, seconds):
            cost = 0

            digits = [minutes // 10, minutes % 10, seconds // 10, seconds % 10]

            start = 0
            for i, digit in enumerate(digits):
                if digit != 0:
                    start = i
                    break

            previous = startAt
            for i in range(start, 4):
                if digits[i] != previous:
                    cost += moveCost
                    previous = digits[i]
                cost += pushCost

            return cost

        cost = 10 ** 9

        minutes = targetSeconds // 60
        seconds = targetSeconds % 60

        if minutes <= 99:
            cost = min(cost, get_cost(minutes, seconds))

        minutes -= 1
        seconds += 60

        if seconds <= 99:
            cost = min(cost, get_cost(minutes, seconds))

        return cost


solution = Solution()
assert solution.minCostSetTime(7, 220, 479, 6000) == 2576
assert solution.minCostSetTime(1, 2, 1, 600) == 6
assert solution.minCostSetTime(0, 1, 2, 76) == 6
