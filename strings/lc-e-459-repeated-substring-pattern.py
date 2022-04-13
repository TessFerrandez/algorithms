class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        def is_repeat(length):
            pattern = s[:length]
            for i in range(length, n - length + 1, length):
                if s[i: i + length] != pattern:
                    return False
            return True

        for i in range(1, n // 2 + 1):
            if n % i != 0:
                continue
            if is_repeat(i):
                return True

        return False


solution = Solution()
assert solution.repeatedSubstringPattern('abab')
assert not solution.repeatedSubstringPattern('aba')
assert solution.repeatedSubstringPattern('abcabcabcabc')
