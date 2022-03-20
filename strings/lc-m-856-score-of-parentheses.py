'''
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
'''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                current = stack.pop()
                if current == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * current

        return stack[0]


solution = Solution()
assert solution.scoreOfParentheses('(()(()))') == 6
assert solution.scoreOfParentheses('((()))()') == 5
assert solution.scoreOfParentheses('()') == 1
assert solution.scoreOfParentheses('()()') == 2
assert solution.scoreOfParentheses('(())') == 2
assert solution.scoreOfParentheses('((()))') == 4
