from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(arr):
            arr = [element for element in arr if element != '.']
            return len(set(arr)) == len(arr)

        def get_columns(board):
            for i in range(9):
                yield [board[j][i] for j in range(9)]

        def get_boxes(board):
            for bc in [0, 3, 6]:
                for br in [0, 3, 6]:
                    box = []
                    for r in range(3):
                        for c in range(3):
                            box.append(board[br + r][bc + c])
                    yield box

        for row in board:
            if not is_valid(row):
                return False

        for column in get_columns(board):
            if not is_valid(column):
                return False

        for box in get_boxes(board):
            if not is_valid(box):
                return False

        return True


solution = Solution()

board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
assert not solution.isValidSudoku(board)

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
assert solution.isValidSudoku(board)

board = [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
assert not solution.isValidSudoku(board)
