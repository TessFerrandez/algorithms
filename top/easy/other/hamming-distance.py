
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binx, biny = '{:032b}'.format(x), '{:032b}'.format(y)
        return sum(1 for i in range(32) if binx[i] != biny[i])


solution = Solution()
assert solution.hammingDistance(1, 4) == 2
assert solution.hammingDistance(3, 1) == 1
