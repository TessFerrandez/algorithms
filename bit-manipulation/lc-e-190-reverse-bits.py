class Solution:
    def reverseBits(self, n: int) -> int:
        b = '{:032b}'.format(n)
        b = ''.join(reversed(b))
        return int(b, 2)


solution = Solution()
assert solution.reverseBits(43261596) == 964176192
assert solution.reverseBits(4294967293) == 3221225471
