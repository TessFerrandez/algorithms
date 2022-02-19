'''
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1

            if d == "0" and not stack:
                continue

            stack.append(d)

        N = len(stack)

        return "0" if N - k <= 0 else ''.join(stack[:N - k])


solution = Solution()
assert solution.removeKdigits("5123636", 3) == "1233"
assert solution.removeKdigits("10200", 1) == "200"
assert solution.removeKdigits("1432219", 3) == "1219"
assert solution.removeKdigits("10", 2) == "0"
