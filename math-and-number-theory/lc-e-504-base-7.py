class Solution:
    def convertToBase7(self, num: int) -> str:
        is_negative = num < 0
        num = abs(num)

        result = ''
        while num > 0:
            result += str(num % 7)
            num = num // 7

        result = result[::-1]
        result = result if result else '0'
        result = '-' + result if is_negative else result
        return result


solution = Solution()
assert solution.convertToBase7(0) == '0'
assert solution.convertToBase7(100) == '202'
assert solution.convertToBase7(-7) == '-10'
