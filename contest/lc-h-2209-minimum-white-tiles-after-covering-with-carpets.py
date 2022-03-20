from functools import cache


class Solution:
    # My solution during contest - TLE
    def minimumWhiteTiles1(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        floor_len = len(floor)

        if numCarpets * carpetLen >= floor_len:
            return 0

        cover = [sum(int(i) for i in floor[:carpetLen])]

        for i in range(carpetLen, floor_len):
            prev = cover[-1]
            cover.append(prev - int(floor[i - carpetLen]) + int(floor[i]))

        whites_left = [0] * floor_len
        curr = 0
        for i in range(floor_len - 1, -1, -1):
            if floor[i] == '1':
                curr += 1
            whites_left[i] = curr

        @cache
        def get_cover(carpets_left, from_i):
            if from_i >= floor_len:
                return 0

            if carpets_left == 0:
                return 0

            if carpets_left * carpetLen > (floor_len - from_i):
                return whites_left[from_i]

            max_cover = 0
            for i in range(from_i, len(cover)):
                max_cover = max(max_cover, cover[i] + get_cover(carpets_left - 1, i + carpetLen))

            return max_cover

        return whites_left[0] - get_cover(numCarpets, 0)

    # cleaned up memoization - maximum recursion
    def minimumWhiteTiles2(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)

        @cache
        def get_min_whites(tile, carpets_left):
            if tile == n - 1:
                if carpets_left == 0:
                    return int(floor[tile])
                else:
                    return 0

            if carpets_left == 0:
                return int(floor[tile]) + get_min_whites(tile + 1, 0)
            if tile + (carpets_left * carpetLen) >= n:
                return 0
            return min(get_min_whites(tile + carpetLen, carpets_left - 1), int(floor[tile]) + get_min_whites(tile + 1, carpets_left))

        return get_min_whites(0, numCarpets)

    # using dynamic programming based on hints
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [[0 for _ in range(numCarpets + 1)] for _ in range(n)]

        dp[n - 1][0] = int(floor[-1])

        for tile in range(n - 2, -1, -1):
            for carpets in range(numCarpets, -1, -1):
                if carpets == 0:
                    dp[tile][0] = dp[tile + 1][0] + int(floor[tile])
                elif tile + (carpets * carpetLen) >= n:
                    continue
                else:
                    dp[tile][carpets] = min(dp[tile + carpetLen][carpets - 1], int(floor[tile]) + dp[tile + 1][carpets])

        return dp[0][numCarpets]


solution = Solution()
assert solution.minimumWhiteTiles('10110101', 2, 2) == 2
assert solution.minimumWhiteTiles('11111', 2, 3) == 0
assert solution.minimumWhiteTiles('10110101', 1, 4) == 2
assert solution.minimumWhiteTiles('101111101', 2, 4) == 1
assert solution.minimumWhiteTiles("1111111111111111111111111101111101111111111111111111111011111111011110111111111111111101111111111001111111110111111111111010111011111111111111111111011111111011111111110111111110111011111111111111110011111111110101111101111011111111111111111111111111111111100111011111111110111111111111011111111111001011111111110010111110101111111111111110111111110111101111111111111111111111011111010110111101110010111111111011111111111111101111111011101111111011110100111011111110111101111111011111111110101011011111111111111111111111001111111011111111011111101111111111111111011111111111111111001111011111110110111011110111110111111101111111111111111111101111110111111011001110011111111111101111101111111110011111111111111110111110110111111111111111111111110111111011101111111111111111101111101101111110111111111111101111111111111111111111101101111111111110111110110111111111111011101011111011110111111111111101111111101101111111111111111111110111111111", 533, 1) == 293
