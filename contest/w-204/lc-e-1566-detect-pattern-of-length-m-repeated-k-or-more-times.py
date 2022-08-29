from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)):
            pattern = arr[i: i + m]
            multi_pattern = pattern * k
            if arr[i: i + k * m] == multi_pattern:
                return True

        return False


solution = Solution()
assert not solution.containsPattern([1, 2, 3, 1, 2], 2, 2)
assert solution.containsPattern([2, 2], 1, 2)
assert solution.containsPattern([1,2,4,4,4,4], 1, 3)
assert solution.containsPattern([1,2,1,2,1,1,1,3], 2, 2)
assert not solution.containsPattern([1,2,1,2,1,3], 2, 3)
