'''
You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.
'''
class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        moves = 0

        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1

        return moves


solution = Solution()
assert solution.minimumMoves('XXX') == 1
assert solution.minimumMoves('XX0X') == 2
assert solution.minimumMoves('0000') == 0
