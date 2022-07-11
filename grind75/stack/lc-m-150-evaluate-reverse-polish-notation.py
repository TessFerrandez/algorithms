from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in '+-*/':
                p2 = stack.pop()
                p1 = stack.pop()

                if token == '+':
                    stack.append(p1 + p2)
                elif token == '-':
                    stack.append(p1 - p2)
                elif token == '*':
                    stack.append(p1 * p2)
                elif token == '/':
                    sign = (-1 if p1 < 0 else 1) * (-1 if p2 < 0 else 1)
                    stack.append((abs(p1) // abs(p2)) * sign)
            else:
                stack.append(int(token))

        return stack[-1]


solution = Solution()
assert solution.evalRPN(["4","-2","/","2","-3","-","-"]) == -7
assert solution.evalRPN(["2","1","+","3","*"]) == 9
assert solution.evalRPN(["4","13","5","/","+"]) == 6
assert solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
