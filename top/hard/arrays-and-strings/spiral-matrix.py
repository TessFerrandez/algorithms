from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []

        if len(matrix) == 0:
            return []

        lowy, highy = 0, len(matrix) - 1
        lowx, highx = 0, len(matrix[0]) - 1

        while lowy <= highy and lowx <= highx:
            # go right
            for col in range(lowx, highx + 1):
                answer.append(matrix[lowy][col])
            lowy += 1

            # go down
            for row in range(lowy, highy + 1):
                answer.append(matrix[row][highx])
            highx -= 1

            # go left
            if lowy <= highy:
                for col in range(highx, lowx - 1, -1):
                    answer.append(matrix[highy][col])
            highy -= 1

            # go up
            if lowx <= highx:
                for row in range(highy, lowy - 1, -1):
                    answer.append(matrix[row][lowx])
            lowx += 1

        return answer


solution = Solution()
assert solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
assert solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
