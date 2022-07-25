from collections import defaultdict
from typing import List
from UnionFind import UnionFind


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        zeros = {(r, c) for r in range(rows) for c in range(cols) if board[r][c] == 'O'}
        if not zeros:
            return

        uf = UnionFind(zeros)
        for r, c in zeros:
            if (r - 1, c) in zeros:
                uf.union((r, c), (r - 1, c))
            if (r, c - 1) in zeros:
                uf.union((r, c), (r, c - 1))

        groups = defaultdict(list)
        borders = set()

        for r, c in zeros:
            parent = uf.find((r, c))
            groups[parent].append((r, c))
            board[r][c] = 'X'
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                borders.add(parent)

        for group in groups:
            if group in borders:
                for r, c in groups[group]:
                    board[r][c] = 'O'

        return board


solution = Solution()

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solution.solve(board)
assert board == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

board = [["X"]]
solution.solve(board)
assert board == [["X"]]
