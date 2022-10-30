from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        bloom = sorted(zip(growTime, plantTime), reverse=True)
        start, max_end = 0, 0

        for grow, plant in bloom:
            start += plant
            max_end = max(max_end, start + grow)

        return max_end


solution = Solution()
assert solution.earliestFullBloom([3,11,29,4,4,26,26,12,13,10,30,19,27,2,10],[10,13,22,17,18,15,21,11,24,14,18,23,1,30,6]) == 227
assert solution.earliestFullBloom([1,4,3], [2,3,1]) == 9
assert solution.earliestFullBloom([1,2,3,2], [2,1,2,1]) == 9
assert solution.earliestFullBloom([1], [1]) == 2
