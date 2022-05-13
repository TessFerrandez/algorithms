class Solution:
    def countVowelStrings1(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(1, n):
            o = o + u
            i = i + o
            e = e + i
            a = a + e

        return a + e + i + o + u

    def countVowelStrings(self, n: int) -> int:
        '''
        4! = 24
        -- number of options in each slot
        '''
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24


solution = Solution()
assert solution.countVowelStrings(1) == 5
assert solution.countVowelStrings(2) == 15
assert solution.countVowelStrings(3) == 35
assert solution.countVowelStrings(4) == 70
assert solution.countVowelStrings(33) == 66045
assert solution.countVowelStrings(50) == 316251
