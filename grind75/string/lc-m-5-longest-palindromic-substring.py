class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best, length = '', 0
        todo = []

        for i in range(n):
            todo.append((i, i))
            if i > 0 and s[i] == s[i - 1]:
                todo.append((i - 1, i))

        while todo:
            l, r = todo.pop()
            if r - l + 1 > length:
                best = s[l: r + 1]
                length = r - l + 1
            if l > 0 and r < n - 1 and s[l - 1] == s[r + 1]:
                todo.append((l - 1, r + 1))

        return best


solution = Solution()
print(solution.longestPalindrome('babad'))
print(solution.longestPalindrome('cbbd'))
