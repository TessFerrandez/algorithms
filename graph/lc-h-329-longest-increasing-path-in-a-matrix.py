from typing import List


class Solution:
    def longestIncreasingPath1(self, matrix: List[List[int]]) -> int:
        longest_path = {}
        rows, cols = len(matrix), len(matrix[0])

        def dfs(row, col):
            if (row, col) in longest_path:
                return longest_path[(row, col)]
            good_neighbors = [(nr, nc) for nr, nc in [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)] if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[row][col]]
            if not good_neighbors:
                longest_path[(row, col)] = 1
            else:
                longest_path[(row, col)] = 1 + max(dfs(nr, nc) for nr, nc in good_neighbors)
            return longest_path[(row, col)]

        return max(dfs(row, col) for row in range(rows) for col in range(cols))

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))


solution = Solution()
assert solution.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]) == 4
assert solution.longestIncreasingPath([[1]]) == 1
