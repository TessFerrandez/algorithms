'''
You are playing a game with integers. You start with the integer 1 and you want to reach the integer target.

In one move, you can either:

Increment the current integer by one (i.e., x = x + 1).
Double the current integer (i.e., x = 2 * x).
You can use the increment operation any number of times, however, you can only use the double operation at most maxDoubles times.

Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.
'''
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0

        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                moves += 1
                target = target // 2
                maxDoubles -= 1
            else:
                if maxDoubles == 0:
                    moves += (target - 1)
                    target = 1
                else:
                    moves += 1
                    target -= 1

        return moves


solution = Solution()
assert solution.minMoves(5, 0) == 4
assert solution.minMoves(19, 2) == 7
assert solution.minMoves(10, 4) == 4
