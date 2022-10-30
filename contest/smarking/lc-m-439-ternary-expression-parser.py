# expression consists of 0-9?:TF
# len <= 10000
# each num is a digit
# conditions group left right to left
# condition will always be T or F, never a digit
# result is either a digit (0-9) or T or F
class Solution:
    def parseTernary1(self, expression: str) -> str:
        self.i = 0

        def parse(expression):
            c = expression[self.i]

            if self.i + 1 == len(expression) or expression[self.i + 1] == ':':
                self.i += 2
                return str(c)

            self.i += 2
            first = parse(expression)
            second = parse(expression)

            return first if c == 'T' else second

        return parse(expression)

    def parseTernary(self, expression: str) -> str:
        n = len(expression)

        def parse(expression, start):
            first_ch = expression[start]

            if start + 1 == n or expression[start + 1] == ':':
                return first_ch, start + 2

            left, next_start = parse(expression, start + 2)
            right, next_start = parse(expression, next_start)

            return left if first_ch == 'T' else right, next_start

        result, _ = parse(expression, 0)
        return result


solution = Solution()
assert solution.parseTernary("T?2:3") == "2"
assert solution.parseTernary("F?1:T?4:5") == "4"
# assert solution.parseTernary("T?T?F:5:3") == "F"
