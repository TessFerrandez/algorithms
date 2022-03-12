class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        result = 0
        for number in numbers:
            while s.startswith(number):
                result += numbers[number]
                s = s[len(number):]
                if s == '':
                    return result
        return result


solution = Solution()
assert solution.romanToInt('MCMXCIV') == 1994
assert solution.romanToInt('III') == 3
assert solution.romanToInt('LVIII') == 58
