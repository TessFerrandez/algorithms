class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = 'a'
        total = 0

        for ch in word:
            moves = abs(ord(ch) - ord(prev))
            moves = min(moves, 26 - moves)
            total += moves + 1
            prev = ch

        return total


solution = Solution()
assert solution.minTimeToType('abc') == 5
assert solution.minTimeToType('bza') == 7
assert solution.minTimeToType('zjpc') == 34
