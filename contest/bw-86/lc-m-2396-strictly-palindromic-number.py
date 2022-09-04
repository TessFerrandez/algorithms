class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def as_base(num, base):
            s = ''
            while num > 0:
                s += str(num % base)
                num = num // base
            return s

        for base in range(2, n - 1):
            representation = as_base(n, base)
            if representation != representation[::-1]:
                return False
        return True

    def isStrictlyPalindromic2(self, n: int) -> bool:
        # the answer will always be false :)
        return False


solution = Solution()
assert not solution.isStrictlyPalindromic(9)
assert not solution.isStrictlyPalindromic(4)
