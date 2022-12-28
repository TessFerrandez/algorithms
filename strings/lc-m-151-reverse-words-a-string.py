class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.split(' ') if word != '']
        return ' '.join(words[::-1])


solution = Solution()
assert solution.reverseWords("the sky is blue") == "blue is sky the"
assert solution.reverseWords("  hello world  ") == "world hello"
assert solution.reverseWords("a good   example") == "example good a"
