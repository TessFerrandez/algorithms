from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []

        if len(matrix) == 0:
            return []

        low_row, high_row = 0, len(matrix) - 1
        low_col, high_col = 0, len(matrix[0]) - 1

        while low_row <= high_row and low_col <= high_col:
            # go right
            for col in range(low_col, high_col + 1):
                answer.append(matrix[low_row][col])
            low_row += 1

            # go down
            for row in range(low_row, high_row + 1):
                answer.append(matrix[row][high_col])
            high_col -= 1

            # go left
            if low_row <= high_row:
                for col in range(high_col, low_col - 1, -1):
                    answer.append(matrix[high_row][col])
            high_row -= 1

            # go up
            if low_col <= high_col:
                for row in range(high_row, low_row - 1, -1):
                    answer.append(matrix[row][low_col])
            low_col += 1

        return answer


solution = Solution()
assert solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
