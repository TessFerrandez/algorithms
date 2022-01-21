class Solution:
    # my solution
    def isPowerOfTwo1(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1

    # bit manipulation
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return not (n & (n - 1))


solution = Solution()
assert solution.isPowerOfTwo(1) == True
assert solution.isPowerOfTwo(16) == True
assert solution.isPowerOfTwo(3) == False
assert solution.isPowerOfTwo(-16) == False
