from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(row, col, word):
            if word == '':
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or word[0] != board[row][col]:
                return False

            ch = board[row][col]
            board[row][col] = '#'       # avoid re-visit

            remaining = word[1:]
            found = dfs(row + 1, col, remaining) or dfs(row - 1, col, remaining) or dfs(row, col + 1, remaining) or dfs(row, col - 1, remaining)
            board[row][col] = ch

            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, word):
                    return True

        return False


solution = Solution()
assert solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
assert solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
assert not solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
