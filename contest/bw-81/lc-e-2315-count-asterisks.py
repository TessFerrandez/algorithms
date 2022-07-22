class Solution:
    def countAsterisks(self, s: str) -> int:
        parts = s.split('|')

        pairs = 0
        for part in parts[::2]:
            pairs += part.count('*')

        return pairs


solution = Solution()
assert solution.countAsterisks("l|*e*et|c**o|*de|") == 2
assert solution.countAsterisks("iamprogrammer") == 0
assert solution.countAsterisks("yo|uar|e**|b|e***au|tifu|l") == 5
