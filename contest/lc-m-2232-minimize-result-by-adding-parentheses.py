class Solution:
    def minimizeResult(self, expression: str) -> str:
        '''
        find the best a * (b + c) * d
        '''
        left, right = expression.split('+')
        left_n, right_n = len(left), len(right)

        best_result = float('inf')
        best_equation = ''

        for i in range(left_n):
            str_a, a = left[:i], 1 if i == 0 else int(left[:i])
            str_b, b = left[i:], int(left[i:])

            for j in range(right_n):
                str_c, c = right[:j + 1], int(right[:j + 1])
                str_d, d = right[j + 1:], 1 if j == right_n - 1 else int(right[j + 1:])
                result = a * (b + c) * d
                if result < best_result:
                    best_result, best_equation = result, str_a + '(' + str_b + '+' + str_c + ')' + str_d

        return best_equation


solution = Solution()
assert solution.minimizeResult("999+999") == '(999+999)'
assert solution.minimizeResult("247+38") == '2(47+38)'
assert solution.minimizeResult("12+34") == '1(2+3)4'
