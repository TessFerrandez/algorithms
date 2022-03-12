class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()

        if s == '':
            return True

        n, mid = len(s), len(s) // 2
        for i in range(mid):
            if s[i] != s[n - i - 1]:
                return False

        return True


solution = Solution()
assert solution.isPalindrome('A man, a plan, a canal: Panama')
assert not solution.isPalindrome('race a car')
assert solution.isPalindrome(' ')
