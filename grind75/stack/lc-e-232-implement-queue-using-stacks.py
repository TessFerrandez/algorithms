class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack = [x] + self.stack

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.stack == []


mq = MyQueue()
mq.push(1)
mq.push(2)
assert mq.peek() == 1
assert mq.pop() == 1
assert not mq.empty()
