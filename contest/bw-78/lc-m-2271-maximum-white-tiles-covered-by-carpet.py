from collections import deque
from itertools import accumulate
from typing import List


class Solution:
    # my contest solution - but this is wrong
    def maximumWhiteTiles1(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        tiles = deque(tiles)

        last_pos = tiles[-1][1] - carpetLen + 1

        current = deque()
        start, end = 0, carpetLen - 1

        while tiles and tiles[0][1] <= end:
            current.append(tiles.popleft())

        whites = sum(min(end, tile[1]) - tile[0] + 1 for tile in current)
        best_whites = whites

        while end <= last_pos:
            start += 1
            end += 1

            if tiles and tiles[0][0] <= end <= tiles[0][1]:
                current.append(tiles.popleft())

            if current and current[0][1] < start:
                current.popleft()
                whites -= 1

            if current:
                if current[0][0] < start:
                    whites -= 1
                if current[-1][1] >= end:
                    whites += 1

            best_whites = max(best_whites, whites)

        return best_whites

    # one pass greedy O(n log n)
    def maximumWhiteTiles2(self, tiles: List[List[int]], carpetLen: int) -> int:
        '''
        optimal carpet cover occurs when left end of the carpet coincides with left end of interval
        '''
        tiles.sort()
        n = len(tiles)

        window = cover = result = 0
        for tile in range(n):
            tile_start, tile_end = tiles[tile]

            # slide the window as far as we can, to fully cover the intervals with the carpet
            while window < n and tiles[window][1] - tile_start + 1 <= carpetLen:
                cover += tiles[window][1] - tiles[window][0] + 1
                window += 1

            # process the remaining carpet
            if window < n and tiles[window][0] - tile_start + 1 <= carpetLen:
                result = max(result, cover + carpetLen - (tiles[window][0] - tile_start))
            else:
                result = max(result, cover)
            if tile != window:
                cover -= tile_end - tile_start + 1

        return result

    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()

        prefix = [0] + list(accumulate(end - start + 1 for start, end in tiles))
        ends = [end for _, end in tiles]

        n = len(ends)
        j = result = 0

        for i in range(n):
            start, _ = tiles[i]     # carpet starts from the beginning of each range
            end = min(ends[-1], start + carpetLen - 1)  # the rightmost index having tile is ends[-1]

            while j < n and ends[j] < end:
                j += 1

            # two cases
            if tiles[j][0] > end:   # right end of carpet doesn't reach the jth range
                result = max(result, prefix[j] - prefix[i])
            else:                   # right end of carpet covers part of the jth range
                result = max(result, prefix[j + 1] - prefix[i] - ends[j] + end)

        return result


solution = Solution()
assert solution.maximumWhiteTiles([[1,5],[10,11],[12,18],[20,25],[30,32]], 10) == 9
# assert solution.maximumWhiteTiles([[10,11],[1,1]], 2) == 2
