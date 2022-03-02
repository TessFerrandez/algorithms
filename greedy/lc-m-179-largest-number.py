from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            return 1 if a + b > b + a else -1

        snums = [str(num) for num in nums]
        snums.sort(key=cmp_to_key(compare), reverse=True)
        result = ''.join(snums)
        if int(result) == 0:
            return '0'
        return result


solution = Solution()
assert solution.largestNumber([0, 0]) == "0"
assert solution.largestNumber([432, 43243]) == "43243432"
assert solution.largestNumber([10, 2]) == '210'
assert solution.largestNumber([3, 30, 34, 5, 9]) == '9534330'
