from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(num) for num in range(1, n + 1)]
        nums.sort()
        return [int(num) for num in nums]


solution = Solution()
assert solution.lexicalOrder(13) == [1,10,11,12,13,2,3,4,5,6,7,8,9]
assert solution.lexicalOrder(2) == [1, 2]
