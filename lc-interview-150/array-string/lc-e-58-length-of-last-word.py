# string

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.split()[-1]
        return len(last_word)


solution = Solution()
assert solution.lengthOfLastWord('Hello World') == 5
assert solution.lengthOfLastWord('   fly me   to   the moon  ') == 4
assert solution.lengthOfLastWord('luffy is still joyboy') == 6
