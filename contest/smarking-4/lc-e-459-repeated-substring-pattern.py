class Solution:
    '''
    examples    s               2s                          2s[1: -1]
                'abab'          'abababab'                  'b(abab)a'
                'aba'           'abaaba'                    'baab'
                'abcabcabcabc'  'abcabcabcabcabcabcabcabc'  'bc(abcabcabcabc)abcabcab'
    '''
    def repeatedSubstringPattern1(self, s: str) -> bool:
        return s in (2 * s)[1: -1]

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1, n // 2 + 1):
            if n % i == 0 and s[: i] * (n // i) == s:
                return True

        return False


solution = Solution()
assert solution.repeatedSubstringPattern('abab')
assert not solution.repeatedSubstringPattern('aba')
assert solution.repeatedSubstringPattern('abcabcabcabc')
