'''
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        c = 1
        while c < n:
            c = c * 2 + 1
        return c - n


solution = Solution()
assert solution.bitwiseComplement(9) == 6   # 1001 - 0110
assert solution.bitwiseComplement(5) == 2   # 101 - 010
assert solution.bitwiseComplement(7) == 0   # 111 - 000
assert solution.bitwiseComplement(10) == 5  # 1010 - 0101
assert solution.bitwiseComplement(4) == 3   # 100 - 011
