class Solution:
    def countEven(self, num: int) -> int:
        sum_tens = sum(int(d) for d in str(num // 10))
        if sum_tens % 2 == 0:
            return num // 2
        if sum_tens % 2 != 0:
            return (num + 1) // 2 - 1


solution = Solution()
assert solution.countEven(123) == 61
assert solution.countEven(63) == 31
assert solution.countEven(20) == 10
assert solution.countEven(4) == 2
assert solution.countEven(30) == 14
assert solution.countEven(31) == 15
