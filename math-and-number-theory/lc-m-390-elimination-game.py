'''
You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Given the integer n, return the last number that remains in arr.
'''
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        return 2 * (1 + n // 2 - self.lastRemaining(n // 2))


solution = Solution()
for i in range(1, 100):
    print(i, solution.lastRemaining(i))
