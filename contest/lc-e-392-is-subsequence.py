class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        j = 0

        for ch in s:
            while j < n and t[j] != ch:
                j += 1

            if j == n:
                return False

            j += 1

        return True


solution = Solution()
assert not solution.isSubsequence('abc', '')
assert not solution.isSubsequence('aaaaaa', 'bbaaaa')
assert solution.isSubsequence('', 'abc')
assert solution.isSubsequence('abc', 'ahbgdc')
assert not solution.isSubsequence('axc', 'ahbgdc')
