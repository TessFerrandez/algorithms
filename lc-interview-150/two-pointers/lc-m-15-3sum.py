# array, two pointers, sorting
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # split the numbers into negative, zero, and positive
        negative, positive, zeros = [], [], []
        for num in nums:
            if num < 0:
                negative.append(num)
            elif num > 0:
                positive.append(num)
            else:
                zeros.append(num)

        negative_set = set(negative)
        positive_set = set(positive)

        # if there is at least 1 zero, add the cases where -num, and num exist => [-num, 0, num]
        result = set()
        if zeros:
            for num in negative_set:
                if -num in positive_set:
                    result.add((num, 0, -num))

        # if there are at least 3 zeros, add [0, 0, 0]
        if len(zeros) >= 3:
            result.add((0, 0, 0))

        # for all pairs of negative numbers, see if the positive of their sum exists (-3, -1, 4)
        for i in range(len(negative)):
            for j in range(i + 1, len(negative)):
                if -(negative[i] + negative[j]) in positive_set:
                    result.add(tuple(sorted([negative[i], negative[j], -(negative[i] + negative[j])])))

        # for all pairs of positive numbers, see if the negative of their sum exists (3, 1, -4)
        for i in range(len(positive)):
            for j in range(i + 1, len(positive)):
                if -(positive[i] + positive[j]) in negative_set:
                    result.add(tuple(sorted([-(positive[i] + positive[j]), positive[i], positive[j]])))

        return sorted([list(result_tuple) for result_tuple in result])


solution = Solution()
assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert solution.threeSum([0, 1, 1]) == []
assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]
