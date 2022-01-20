class Solution:
    def hammingWeight(self, n: int) -> int:
        bstr = bin(n)
        return sum(1 for ch in bstr if ch == '1')




solution = Solution()
assert solution.hammingWeight(int('00000000000000000000000000001011', 2)) == 3
assert solution.hammingWeight(int('00000000000000000000000010000000', 2)) == 1
assert solution.hammingWeight(int('11111111111111111111111111111101', 2)) == 31
