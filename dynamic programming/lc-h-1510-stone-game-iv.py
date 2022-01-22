'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.
'''
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {0: False}

        def dp(n):
            if n not in memo:
                i = 1
                memo[n] = False
                while i * i <= n:
                    if dp(n - i*i) == False:
                        memo[n] = True
                        break
                    i += 1

            return memo[n]

        return dp(n)


solution = Solution()
assert solution.winnerSquareGame(1) == True
assert solution.winnerSquareGame(2) == False
assert solution.winnerSquareGame(3) == True
assert solution.winnerSquareGame(4) == True
assert solution.winnerSquareGame(5) == False
assert solution.winnerSquareGame(6) == True
assert solution.winnerSquareGame(7) == False
