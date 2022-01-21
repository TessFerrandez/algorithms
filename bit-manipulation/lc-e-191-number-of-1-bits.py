class Solution:
    # my solution
    # loops 32 times (for the count)
    def hammingWeight1(self, n: int) -> int:
        return bin(n).count('1')

    # bit manipulation - cuts out the least significant 1 in each round
    # ex. 1001 & 1000 (9 & 8)  0001
    # ex. 1000 & 0111 (8 & 7)  0000
    # ex. 111 & 110   (7 & 6)  110
    # only loops as many times as there are 1s
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count


solution = Solution()
assert solution.hammingWeight(int('00000000000000000000000000001011', 2)) == 3
assert solution.hammingWeight(int('00000000000000000000000010000000', 2)) == 1
assert solution.hammingWeight(int('11111111111111111111111111111101', 2)) == 31
