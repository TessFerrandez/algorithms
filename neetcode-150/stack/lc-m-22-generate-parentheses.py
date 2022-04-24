from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, result = [], []

        def backtrack(open, closed):
            if open == closed == n:
                result.append(''.join(stack))
                return

            if open < n:
                stack.append('(')
                backtrack(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(')')
                backtrack(open, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return result


solution = Solution()
assert solution.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
assert solution.generateParenthesis(1) == ["()"]
