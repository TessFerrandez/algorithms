from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False

        def dfs(row, col, i):
            if self.found:
                return

            if i == n:
                self.found = True
                return

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            temp = board[row][col]
            if temp != word[i]:
                return

            board[row][col] = '#'

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                dfs(row + dy, col + dx, i + 1)

            board[row][col] = temp

        rows, cols, n = len(board), len(board[0]), len(word)

        for r in range(rows):
            for c in range(cols):
                if self.found:
                    return True
                dfs(r, c, 0)

        return self.found


solution = Solution()
assert solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCE')
assert solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE')
assert not solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB')
