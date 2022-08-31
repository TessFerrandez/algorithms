class Solution:
    def findComplement(self, num: int) -> int:
        bin_representation = bin(num)[2:]
        complement = ''.join(['1' if n == '0' else '0' for n in bin_representation])
        return int(complement, 2)


solution = Solution()
assert solution.findComplement(5) == 2
assert solution.findComplement(1) == 0
