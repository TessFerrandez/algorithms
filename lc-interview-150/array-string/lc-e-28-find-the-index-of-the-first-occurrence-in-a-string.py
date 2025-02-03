# two pointers, string, string matching
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


solution = Solution()
assert solution.strStr("sadbutsad", "sad") == 0
assert solution.strStr("leetcode", "leeto") == -1
assert solution.strStr("hello", "ll") == 2
