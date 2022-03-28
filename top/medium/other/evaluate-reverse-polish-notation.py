from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                sign = (-1 if b < 0 else 1) * (-1 if a < 0 else 1)
                stack.append((abs(b) // abs(a)) * sign)
            else:
                stack.append(int(token))

        return stack.pop()


solution = Solution()
assert solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
assert solution.evalRPN(["2","1","+","3","*"]) == 9
assert solution.evalRPN(["4","13","5","/","+"]) == 6
