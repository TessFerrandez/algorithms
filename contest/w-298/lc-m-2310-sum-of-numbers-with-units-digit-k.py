class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        '''
        Assume set is A1 + A2 + ... + An = Sum
        So A1 + A2 + ... + An = n * k + 10 * (a1 + a2 + ... + an) = sum
        where (a1 + a2 + ... + an) can be any number

        ex. sum = 58, k = 9
        n * k = 2 * 9 = 18 and 10 * (a1 + a2) = 58 - 18 = 40. So a1 + a2 = 4
        Find the minimum number satisfying the condition (n * k) % 10 == sum % 10, because 10 * (a1 + a2 + ... + an) % 10 will always be 0
        '''
        if num == 0:
            return 0

        for n in range(1, 11):
            if n * k % 10 == num % 10 and n * k <= num:
                return n

        return -1


solution = Solution()
assert solution.minimumNumbers(4, 0) == -1
assert solution.minimumNumbers(58, 9) == 2
assert solution.minimumNumbers(37, 2) == -1
assert solution.minimumNumbers(0, 7) == 0
assert solution.minimumNumbers(35, 5) == 1
assert solution.minimumNumbers(21, 7) == 3
