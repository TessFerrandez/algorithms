from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        '''
        40 = 2*2*2*5 = [3, 1] => min(3, 1) = 1 => 1 traling zero
        1500 = 3*2*2*5*5*5 = [2, 3] => 2 trailing
        40 * 1500 = [5, 4] => 4 trailing

        Best = top/left, top/right, bottom/left, bottom/right
        '''
        rows, cols = len(grid), len(grid[0])
        vertical = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        horizontal = [[[0, 0] for _ in range(cols)] for _ in range(rows)]

        def f25(num):
            '''2 and 5 factors'''
            f2, f5 = 0, 0

            while num % 2 == 0:
                num //= 2
                f2 += 1

            while num % 5 == 0:
                num //= 5
                f5 += 1

            return [f2, f5]

        for row in range(rows):
            for col in range(cols):
                if col == 0:
                    vertical[row][col] = f25(grid[row][col])
                else:
                    f2, f5 = f25(grid[row][col])
                    vertical[row][col][0] = vertical[row][col - 1][0] + f2
                    vertical[row][col][1] = vertical[row][col - 1][1] + f5

        for col in range(cols):
            for row in range(rows):
                if row == 0:
                    horizontal[row][col] = f25(grid[row][col])
                else:
                    f2, f5, = f25(grid[row][col])
                    horizontal[row][col][0] = horizontal[row - 1][col][0] + f2
                    horizontal[row][col][1] = horizontal[row - 1][col][1] + f5

        result = 0
        for row in range(rows):
            for col in range(cols):
                h2, h5 = horizontal[rows - 1][col]
                v2, v5 = vertical[row][cols - 1]
                c2, c5 = f25(grid[row][col])
                hc2, hc5 = horizontal[row][col]
                vc2, vc5 = vertical[row][col]

                top_left = [hc2 + vc2 - c2, hc5 + vc5 - c5]
                result = max(result, min(top_left))

                top_right = [v2 - vc2 + hc2, v5 - vc5 + hc5]
                result = max(result, min(top_right))

                bottom_left = [h2 - hc2 + vc2, h5 - hc5 + vc5]
                result = max(result, min(bottom_left))

                bottom_right = [h2 + v2 - hc2 - vc2 + c2, h5 + v5 - hc5 - vc5 + c5]
                result = max(result, min(bottom_right))

        return result


solution = Solution()
assert solution.maxTrailingZeros([[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]) == 3
assert solution.maxTrailingZeros([[4,3,2],[7,6,1],[8,8,8]]) == 0
