from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.max_value, self.bobs_arrows = 0, []

        def dfs(arrows_left, current_result, bobs_arrows, current_point):
            if arrows_left == 0:
                if current_result >= self.max_value:
                    self.max_value = current_result
                    self.bobs_arrows = bobs_arrows[:]

            if arrows_left < 0 or current_point < 0:
                return

            for point in range(current_point, -1, -1):
                if point == 0:
                    bobs_arrows[point] = arrows_left
                    if current_result >= self.max_value:
                        self.max_value = current_result
                        self.bobs_arrows = bobs_arrows[:]
                        break

                arrows_needed = aliceArrows[point] + 1

                # try taking this point
                arrows_left = arrows_left - arrows_needed
                current_result += point
                bobs_arrows[point] += arrows_needed

                dfs(arrows_left, current_result, bobs_arrows, point - 1)

                # backtrack
                arrows_left += arrows_needed
                current_result -= point
                bobs_arrows[point] = 0

        dfs(numArrows, 0, [0 for _ in range(12)], 11)
        return self.bobs_arrows


solution = Solution()
assert solution.maximumBobPoints(9, [1,1,0,1,0,0,2,1,0,1,2,0]) == [0,0,0,0,1,1,0,0,1,2,3,1]
assert solution.maximumBobPoints(3, [0,0,1,0,0,0,0,0,0,0,0,2]) == [0,0,0,0,0,0,0,0,1,1,1,0]
