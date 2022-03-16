from collections import deque


class Solution:
    def longestPalindrome1(self, s: str) -> str:
        n = len(s)

        todo = deque([])

        for i in range(len(s) - 1):
            todo.append((1, i, i))
            if s[i] == s[i + 1]:
                todo.append((2, i, i + 1))
        todo.append((1, n - 1, n - 1))

        max_len = 0
        best = ''
        while todo:
            slen, start, end = todo.popleft()
            if slen > max_len:
                max_len = slen
                best = s[start: end + 1]

            if start > 0 and end < n - 1 and s[start - 1] == s[end + 1]:
                todo.append((slen + 2, start - 1, end + 1))

        return best

    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(s, i1, i2):
            while i1 >= 0 and i2 < len(s) and s[i1] == s[i2]:
                i1 -= 1
                i2 += 1
            return i2 - i1 - 1

        if s == '':
            return s

        start, end = 0, 0
        for i in range(len(s)):
            len1 = expand_from_center(s, i, i)
            len2 = expand_from_center(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start: end + 1]


solution = Solution()
result = solution.longestPalindrome('babad')
assert result == 'bab' or result == 'aba'
assert solution.longestPalindrome('cbbd') == 'bb'
