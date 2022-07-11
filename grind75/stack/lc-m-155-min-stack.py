from sys import maxsize


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val, min(self.getMin(), val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        if not self.stack:
            return maxsize
        return self.stack[-1][1]


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
assert stack.getMin() == -3
stack.pop()
assert stack.top() == 0
assert stack.getMin() == -2
