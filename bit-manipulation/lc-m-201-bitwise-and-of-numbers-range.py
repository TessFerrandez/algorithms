'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Ex. [4, 7]
100
101
110
111
-> 100

Find the common ones in the beginning
The rest are 0s
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right or left == 0:
            return left

        bin_left, bin_right = bin(left)[2:], bin(right)[2:]

        if len(bin_left) != len(bin_right):
            return 0

        i = 0
        result = ''
        while bin_left[i] == bin_right[i]:
            result += bin_left[i]
            i += 1

        zeros = len(bin_left) - len(result)
        result += '0' * zeros
        return int(result, 2)


solution = Solution()
assert solution.rangeBitwiseAnd(5, 7) == 4
assert solution.rangeBitwiseAnd(0, 0) == 0
assert solution.rangeBitwiseAnd(1, 2147483647) == 0
assert solution.rangeBitwiseAnd(10, 11) == 10
