# two pointers, string
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return ' '.join(reversed(words))


solution = Solution()
assert solution.reverseWords("the sky is blue") == "blue is sky the"
assert solution.reverseWords("  hello world  ") == "world hello"
assert solution.reverseWords("a good    example") == "example good a"
