class Solution:
    def reverseBits(self, n: int) -> int:
        b = '{:032b}'.format(n)
        b = ''.join(reversed(b))
        return int(b, 2)


solution = Solution()
assert solution.reverseBits(int('00000010100101000001111010011100', 2)) == 964176192
assert solution.reverseBits(int('11111111111111111111111111111101', 2)) == 3221225471
