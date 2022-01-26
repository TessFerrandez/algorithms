class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reversed_words = [''.join(list(reversed(word))) for word in words]
        return ' '.join(reversed_words)


solution = Solution()
assert solution.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
