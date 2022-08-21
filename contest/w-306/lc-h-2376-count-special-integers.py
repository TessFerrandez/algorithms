from functools import reduce


class Solution:
    def countSpecialNumbers1(self, n: int) -> int:
        def count(i, start=9):
            if i == 0:
                return start
            return (start - i) * count(i - 1, start)

        def dfs(i, mask, sn):
            if i >= len(sn):
                return 1
            res, curr = 0, int(sn[i])
            for j in range(1 if i == 0 else 0, curr):
                if mask & (1 << j) == 0:
                    res += count(len(sn) - 2 - i, 9 - i) if len(sn) - 2 - i >= 0 else 1

            if mask & (1 << curr) == 0:
                res += dfs(i + 1, mask + (1 << curr), sn)
            return res

        if n < 10:
            return n
        res = 9
        sn = str(n)
        for i in range(len(sn) - 2):
            res += 9 * count(i)
        return res + dfs(0, 0, sn)

    # O(n2) - permutation and combo digit by digit -- n <= 10
    def countSpecialNumbers(self, n: int) -> int:
        '''
        Ex. 3978
        1. Count special < 1000 (see LC 357 => 9 * 9 * 8 = 648)
        2. Count special in [1000, 3000) by fixing first digit [1, 3)
            times with any that don't have duplicate digits (2 for first digit (1, 2), 9 for 2nd (excluding what was chosen for first), 8 for 3rd, 7 for 4th - 2 * 9 * 8 * 7 = 1008)
        3. Count special in [3000, 3700) by enumerating 2nd from [0, 7) except 3 -- first fixed at 3, 2nd choose from 6, 34d choose from 8, 4th from 7 = 6 * 7 * 8 = 336
        4. Count special in [3700, 3790) fix third [0, 9) excluding 3 and 7 so 8*7 = 56
        5. Count special in [3790, 3798) for last digit choose [0, 8) except 3, 7, 8 = 5
        6. Dont forget 3798 itself

        Be careful with leading 0
        '''
        def f(n):
            if n == 0:
                return 0
            # 1 <= special numbers < 10 ^ n
            result = temp = 9
            for i in range(n - 1):
                temp *= (9 - i)
                result += temp
            return result

        nums = list(map(int, str(n)))
        n = len(nums)
        result = f(n - 1)
        seen = set()

        for i, num in enumerate(nums):
            # fix the i-th digit: ___ (0) ... <= special numbers <= ___ (num - 1)
            initials = len([j for j in range(max(1 - i, 0), num) if j not in seen])

            # candidates for tail part
            k = 9 - len(seen)
            result += initials * reduce(lambda x, y: x * y, range(k, k - (n - 1 - i), - 1), 1)
            if num in seen:
                # no numbers can start with nums[: i + 1] now
                return result

            seen.add(num)

        return result + 1


solution = Solution()
assert solution.countSpecialNumbers(20) == 19
assert solution.countSpecialNumbers(5) == 5
assert solution.countSpecialNumbers(135) == 110
