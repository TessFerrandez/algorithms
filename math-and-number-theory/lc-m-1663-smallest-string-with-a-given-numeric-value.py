class Solution:
    def getSmallestString1(self, n: int, k: int) -> str:
        result = ['a'] * n

        k = k - n
        i = n - 1

        while k:
            k += 1

            if k // 26 >= 1:
                result[i] = 'z'
                k -= 26
                i -= 1
            else:
                result[i] = chr(k + 96)
                k = 0

        return ''.join(result)

    def getSmallestString2(self, n: int, k: int) -> str:
        value_left = k
        z_count = 0

        while value_left > (n - 1) + 25:
            z_count += 1
            value_left -= 26
            n -= 1

        middle_char = ''
        if n > 0 and value_left > n:
            middle_char = chr(value_left - n + 97)
            n -= 1

        return 'a' * n + middle_char + 'z' * z_count

    def getSmallestString(self, n: int, k: int) -> str:
        z_count, rest = divmod(k - n, 25)
        return ('' if z_count == n else 'a' * (n - z_count - 1) + chr(ord('a') + rest)) + 'z' * z_count


solution = Solution()
assert solution.getSmallestString(3, 27) == 'aay'
assert solution.getSmallestString(5, 130) == 'zzzzz'
assert solution.getSmallestString(3, 28) == 'aaz'
assert solution.getSmallestString(5, 73) == 'aaszz'
