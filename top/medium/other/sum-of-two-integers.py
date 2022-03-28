from math import log2


class Solution:
    # TLE (-1) Bit manipulation
    def getSum1(self, a: int, b: int) -> int:
        result = ''

        rest = 0
        while a > 0 or b > 0 or rest > 0:
            last_a, last_b = a % 2, b % 2
            bit_sum = last_a + last_b + rest
            if bit_sum == 3:
                result = '1' + result
                rest = 1
            elif bit_sum == 2:
                result = '0' + result
                rest = 1
            elif bit_sum == 1:
                result = '1' + result
                rest = 0
            else:
                result = '0' + result
                rest = 0
            a = a // 2
            b = b // 2

        return int(result, 2)

    # magic
    def getSum2(self, a: int, b: int) -> int:
        return int(log2(2**a * 2**b))

    # bit manipulation - round 2 - doesnt work for negative
    def getSum3(self, a: int, b: int) -> int:
        carry = 0
        result = 0

        for i in range(32):
            lasta, lastb = (a >> i) & 1, (b >> i) & 1

            if (lasta & lastb) == 1:
                result = result | (carry << i)
                carry = 1
            elif (lasta | lastb) == 0:
                result = result | (carry << i)
                carry = 0
            elif carry == 0:
                # 1 with no carry
                result |= (1 << i)

        return result

    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while b:
            bit_sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = bit_sum
            b = carry

        if (a >> 31) & 1:   # If a is negative in 32 bits sense
            return ~(a ^ mask)

        return a


solution = Solution()
assert solution.getSum(1, 2) == 3
assert solution.getSum(2, 3) == 5
assert solution.getSum(-1, 1) == 0
