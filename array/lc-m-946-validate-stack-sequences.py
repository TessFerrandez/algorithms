from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushed.reverse()
        popped.reverse()

        while popped:
            next_pop = popped.pop()
            if stack and stack[-1] == next_pop:
                stack.pop()
            else:
                while pushed and pushed[-1] != next_pop:
                    stack.append(pushed.pop())
                if not pushed:
                    return False
                pushed.pop()

        if pushed:
            return False

        return True


solution = Solution()
assert solution.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
assert not solution.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
