'''
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
'''
class Solution:
    def minPartitions(self, n: str) -> int:
        min_partitions = 0

        for digit in n:
            min_partitions = max(min_partitions, int(digit))

        return min_partitions


solution = Solution()
assert solution.minPartitions('32') == 3
assert solution.minPartitions('82734') == 8
assert solution.minPartitions('27346209830709182346') == 9
