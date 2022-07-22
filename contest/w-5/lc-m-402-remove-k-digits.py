class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            digit = int(d)
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0 and stack:
            stack.pop()
            k -= 1

        if not stack:
            return '0'
        return str(int(''.join(str(d) for d in stack)))


solution = Solution()
assert solution.removeKdigits("1432219", 3) == '1219'
assert solution.removeKdigits("10200", 1) == '200'
assert solution.removeKdigits("10", 2) == '0'
assert solution.removeKdigits('199', 1) == '19'
assert solution.removeKdigits('198', 1) == '18'
assert solution.removeKdigits('189', 1) == '18'
