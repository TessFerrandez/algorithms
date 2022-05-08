from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        tmp = deque([x])
        tmp.extend(self.queue)
        self.queue = tmp

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
assert stack.top() == 2
assert stack.pop() == 2
assert not stack.empty()
