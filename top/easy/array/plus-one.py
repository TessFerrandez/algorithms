from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        rest = 1

        while digits:
            digit = digits.pop()
            digit += rest
            if digit >= 10:
                rest = 1
            else:
                rest = 0
            result.append(digit % 10)

        if rest == 1:
            result.append(1)

        result.reverse()
        return result


solution = Solution()
assert solution.plusOne([1, 2, 3]) == [1, 2, 4]
assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
assert solution.plusOne([9]) == [1, 0]
