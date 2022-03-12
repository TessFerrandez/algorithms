class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        if len(needle) > len(haystack):
            return -1

        nn = len(needle)

        for i in range(len(haystack) - nn + 1):
            if haystack[i: i + nn] == needle:
                return i
        return -1


solution = Solution()
assert solution.strStr('hello', 'll') == 2
assert solution.strStr('aaaa', 'baa') == -1
assert solution.strStr('', '') == 0
