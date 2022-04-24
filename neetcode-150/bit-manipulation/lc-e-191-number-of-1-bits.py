class Solution:
    # built-in
    def hammingWeight1(self, n: int) -> int:
        return bin(n).count('1')

    # using bit operations
    def hammingWeight(self, n: int) -> int:
        '''
        ex. 11
        1011
        1010 (1)
        ----
        1010
        1001 (2)
        ----
        1000
        0111 (3)
        ----
        0000 DONE
        '''
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count


solution = Solution()
assert solution.hammingWeight(11) == 3
assert solution.hammingWeight(32) == 1
assert solution.hammingWeight(4294967293) == 31
