class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        for i in range(k):
            if blocks[i] == 'W':
                whites += 1
        best_whites = whites

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                whites -= 1
            if blocks[i] == 'W':
                whites += 1
            best_whites = min(best_whites, whites)

        return best_whites


solution = Solution()
assert solution.minimumRecolors("WBBWWBBWBW", 7) == 3
assert solution.minimumRecolors("WBWBBBW", 2) == 0
