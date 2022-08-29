class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        bin_n = bin(n)

        if bin_n.count('1') != 1:
            return False

        pos = bin_n[::-1].find('1')

        return pos % 2 == 0


solution = Solution()
assert solution.isPowerOfFour(16)
assert not solution.isPowerOfFour(5)
assert solution.isPowerOfFour(1)
assert not solution.isPowerOfFour(-64)
