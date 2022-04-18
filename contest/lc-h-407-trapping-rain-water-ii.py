from typing import List
from heapq import heappop, heappush


class Solution:
    def trapRainWater1(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])

        maxleft = [[0 for _ in range(cols)] for _ in range(rows)]
        maxright = [[0 for _ in range(cols)] for _ in range(rows)]
        maxtop = [[0 for _ in range(cols)] for _ in range(rows)]
        maxbottom = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            highest = 0
            for col in range(cols):
                highest = max(heightMap[row][col], highest)
                maxleft[row][col] = highest

            highest = 0
            for col in range(cols - 1, -1, -1):
                highest = max(highest, heightMap[row][col])
                maxright[row][col] = highest

        for col in range(cols):
            highest = 0
            for row in range(rows):
                highest = max(highest, heightMap[row][col])
                maxtop[row][col] = highest

            highest = 0
            for row in range(rows - 1, -1, -1):
                highest = max(highest, heightMap[row][col])
                maxbottom[row][col] = highest

        trapped = 0
        for row in range(rows):
            for col in range(cols):
                walls = min(min(min(maxleft[row][col], maxright[row][col]), maxtop[row][col]), maxbottom[row][col])
                current = heightMap[row][col]
                if current < walls:
                    print(row, col, walls, current, walls - current)
                    trapped += walls - current

        # print(maxleft)
        # print(maxright)
        # print(maxtop)
        # print(maxbottom)
        return trapped

    # BFS solution using heap
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        # Initial
        # Board cells cannot trap the water
        rows, cols = len(heightMap), len(heightMap[0])
        if rows < 3 or cols < 3:
            return 0

        # Add Board cells first
        heap = []
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    heappush(heap, (heightMap[row][col], row, col))
                    heightMap[row][col] = -1

        # Start from level 0
        level, trapped = 0, 0

        while heap:
            height, y, x = heappop(heap)
            level = max(height, level)

            for row, col in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
                if 0 <= row < rows and 0 <= col < cols and heightMap[row][col] != -1:
                    heappush(heap, (heightMap[row][col], row, col))

                    # If cell's height smaller than the level, then it can trap the rain water
                    if heightMap[row][col] < level:
                        trapped += level - heightMap[row][col]

                    # Set the height to -1 if the cell is visited
                    heightMap[row][col] = -1

        return trapped


solution = Solution()
assert solution.trapRainWater([[5,5,5,1],[5,1,1,5],[5,1,5,5],[5,2,5,8]]) == 3
assert solution.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]) == 14
assert solution.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]) == 4
assert solution.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]) == 10
