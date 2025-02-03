# hash table math string
class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        roman = ''

        for val, char in numerals:
            if num == 0:
                return roman
            while num >= val:
                num -= val
                roman += char
        return roman


solution = Solution()
assert solution.intToRoman(3749) == 'MMMDCCXLIX'
assert solution.intToRoman(58) == 'LVIII'
assert solution.intToRoman(1994) == 'MCMXCIV'
