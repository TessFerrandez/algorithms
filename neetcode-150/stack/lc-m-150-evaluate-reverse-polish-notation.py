from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in '+-/*':
                v2 = stack.pop()
                v1 = stack.pop()
            if token == '+':
                stack.append(v1 + v2)
            elif token == '-':
                stack.append(v1 - v2)
            elif token == '*':
                stack.append(v1 * v2)
            elif token == '/':
                sign = (-1 if v2 < 0 else 1) * (-1 if v1 < 0 else 1)
                stack.append((abs(v1) // abs(v2)) * sign)
            else:
                stack.append(int(token))

        return stack[0]


solution = Solution()
assert solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
assert solution.evalRPN(["2","1","+","3","*"]) == 9
assert solution.evalRPN(["4","13","5","/","+"]) == 6
