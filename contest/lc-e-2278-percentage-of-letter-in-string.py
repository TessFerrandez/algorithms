class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        pct = (s.count(letter) / len(s)) * 100
        return int(pct)


solution = Solution()
assert solution.percentageLetter('sgawtb', 's') == 16
assert solution.percentageLetter('foobar', 'o') == 33
assert solution.percentageLetter('jjjj', 'k') == 0
