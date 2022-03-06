class Solution:
    def freqAlphabets(self, s: str) -> str:
        translator = {}

        i = 1
        for ch in 'abcdefghi':
            translator[str(i)] = ch
            i += 1
        for ch in 'jklmnopqrstuvwxyz':
            translator[str(i) + '#'] = ch
            i += 1

        translated = ''
        n = len(s)
        while n > 0:
            if n >= 3 and s[2] == '#':
                translated += translator[s[:3]]
                s = s[3:]
                n -= 3
            else:
                translated += translator[s[0]]
                s = s[1:]
                n -= 1

        return translated


solution = Solution()
assert solution.freqAlphabets('10#11#12') == 'jkab'
assert solution.freqAlphabets('1326#') == 'acz'
