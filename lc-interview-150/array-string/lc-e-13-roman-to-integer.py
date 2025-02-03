# hash table, math, string
class Solution:
    def romanToInt(self, s: str) -> int:
        str_len = len(s)
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        number = 0
        while s:
            if len(s) >= 2 and s[:2] in roman_to_int:
                number += roman_to_int[s[:2]]
                s = s[2:]
            else:
                number += roman_to_int[s[0]]
                s = s[1:]

        return number


solution = Solution()
assert solution.romanToInt('III') == 3
assert solution.romanToInt('IV') == 4
assert solution.romanToInt('IX') == 9
assert solution.romanToInt('LVIII') == 58
assert solution.romanToInt('MCMXCIV') == 1994
