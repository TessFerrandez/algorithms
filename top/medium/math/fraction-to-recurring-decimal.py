class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        sign = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)

        result = sign + str(numerator // denominator) + '.'

        numerator %= denominator
        i, part = 0, ''
        m = {numerator: i}

        while numerator % denominator:
            numerator *= 10
            i += 1
            remainder = numerator % denominator
            part += str(numerator // denominator)

            if remainder in m:
                part = part[:m[remainder]] + '(' + part[m[remainder]:] + ')'
                return result + part

            m[remainder] = i
            numerator = remainder

        return result + part


solution = Solution()
assert solution.fractionToDecimal(2, 1) == "2"
assert solution.fractionToDecimal(1, 2) == "0.5"
assert solution.fractionToDecimal(4, 333) == "0.(012)"
