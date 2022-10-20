class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)

        sum = ""
        rest = 0
        while num1 or num2:
            current = 0
            if num1:
                current += int(num1.pop())
            if num2:
                current += int(num2.pop())
            current += rest
            if current >= 10:
                rest = current // 10
                current = current % 10
            else:
                rest = 0
            sum += str(current)
        if rest:
            sum += str(rest)
        return sum[::-1]


solution = Solution()
assert solution.addStrings("11", "123") == "134"
assert solution.addStrings("456", "77") == "533"
assert solution.addStrings("0", "0") == "0"
