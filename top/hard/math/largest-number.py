from typing import List


class NumComparer(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        str_nums = sorted(str_nums, key=NumComparer)
        return str(int(''.join(str_nums)))


solution = Solution()
assert solution.largestNumber([0, 0]) == '0'
assert solution.largestNumber([10, 2]) == '210'
assert solution.largestNumber([3, 30, 34, 5, 9]) == '9534330'
assert solution.largestNumber([3, 30, 34, 5, 9, 340]) == '9534340330'
assert solution.largestNumber([111311, 1113]) == '1113111311'
