from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            temp = nums.pop()
            nums.insert(0, temp)


solution = Solution()

arr = [1,2,3,4,5,6,7]
solution.rotate(arr, 3)
assert arr == [5,6,7,1,2,3,4]
