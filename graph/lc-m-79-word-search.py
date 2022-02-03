'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.
'''
from itertools import product
from typing import List


class Solution:
    def exist2(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, row, col):
            if self.Found:
                return

            if index == word_len:
                self.Found = True
                return

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            temp = board[row][col]
            if temp != word[index]:
                return

            board[row][col] = "#"           # this way we don't have to keep a set of visited
            for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                dfs(index + 1, row + dy, col + dx)

            board[row][col] = temp

        self.Found = False
        rows, cols, word_len = len(board), len(board[0]), len(word)

        for row, col in product(range(rows), range(cols)):
            if self.Found:
                return True
            dfs(0, row, col)

        return self.Found

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def in_grid(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            return True

        def has_path(board, row, col, word):
            if len(word) == 0:
                return True

            if not in_grid(row, col) or board[row][col] != word[0]:
                return False

            temp = board[row][col]
            board[row][col] = "#"

            result = has_path(board, row + 1, col, word[1:]) or has_path(board, row - 1, col, word[1:]) or has_path(board, row, col + 1, word[1:]) or has_path(board, row, col - 1, word[1:])

            board[row][col] = temp

            return result

        for row in range(rows):
            for col in range(cols):
                if has_path(board, row, col, word):
                    return True

        return False


solution = Solution()
assert solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
assert solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
assert not solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
