'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
from itertools import zip_longest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def multiply_single(d2, zeros, num1):
            result = [0] * zeros
            carry = 0

            for d1 in num1:
                product = int(d1) * int(d2) + carry
                carry = product // 10
                result.append(product % 10)

            if carry:
                result.append(carry)

            return result

        def sum_products(products):
            result = products.pop()

            for product in products:
                current_result = []
                carry = 0

                for d1, d2 in zip_longest(product, result, fillvalue=0):
                    current_sum = d1 + d2 + carry
                    carry = current_sum // 10
                    current_result.append(current_sum % 10)

                if carry:
                    current_result.append(carry)

                result = current_result

            return ''.join(str(digit) for digit in result[::-1])

        if num1 == '0' or num2 == '0':
            return '0'

        num1, num2 = num1[::-1], num2[::-1]

        products = []
        for i, digit in enumerate(num2):
            products.append(multiply_single(digit, i, num1))

        result = sum_products(products)
        return result


solution = Solution()
assert solution.multiply('123', '456') == '56088'
assert solution.multiply('2', '3') == '6'
