class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


solution = Solution()
assert solution.hammingWeight(11) == 3
assert solution.hammingWeight(128) == 1
assert solution.hammingWeight(4294967293) == 31
