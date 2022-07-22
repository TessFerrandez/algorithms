from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        '''
        binary search solution - we try to find d (largest distance)
        count_balls_placed(d) returns number of balls we can place with this distance
        '''
        n = len(position)
        position.sort()

        def count_balls_placed(distance):
            balls_placed, current = 1, position[0]
            for i in range(1, n):
                if position[i] - current >= distance:
                    balls_placed += 1
                    current = position[i]
            return balls_placed

        low, high = 0, position[-1] - position[0]
        while low < high:
            mid = high - (high - low) // 2
            if count_balls_placed(mid) >= m:
                low = mid
            else:
                high = mid - 1

        return low


solution = Solution()
assert solution.maxDistance([1,2,3,4,7], m=3) == 3
assert solution.maxDistance([5,4,3,2,1,1000000000], m=2) == 999999999
