from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    # my accepted solution
    def maximumRows1(self, mat: List[List[int]], cols: int) -> int:
        rows = len(mat)
        all_cols = len(mat[0])
        col_rows = defaultdict(set)

        for row in range(rows):
            for col in range(all_cols):
                if mat[row][col] == 1:
                    col_rows[col].add(row)

        best_option = 0
        for combo in combinations(range(all_cols), cols):
            false_rows = set()
            for col in range(all_cols):
                if col not in combo:
                    false_rows |= col_rows[col]
            best_option = max(best_option, rows - len(false_rows))

        return best_option

    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        all_cols = len(mat[0])
        max_rows = 0

        col_combos = list(combinations(list(range(all_cols)), cols))

        for selected_cols in col_combos:
            selected_cols = set(selected_cols)
            row_hidden = 0
            for row in mat:
                can_hide = True
                for col in range(all_cols):
                    if row[col] and col not in selected_cols:
                        can_hide = False
                        break
                if can_hide:
                    row_hidden += 1
            max_rows = max(max_rows, row_hidden)
        return max_rows


solution = Solution()
assert solution.maximumRows([[0,0,0],[1,0,1],[0,1,1],[0,0,1]], 2) == 3
assert solution.maximumRows([[1],[0]], 1) == 2
