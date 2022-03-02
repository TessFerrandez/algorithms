'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum:
            self.minimum.append(val)
        else:
            self.minimum.append(min(self.minimum[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


min_stack = MinStack()
min_stack.push(-2)
min_stack.push(4)
min_stack.push(0)
min_stack.push(-3)
assert min_stack.getMin() == -3
min_stack.pop()
assert min_stack.top() == 0
assert min_stack.getMin() == -2
min_stack.pop()
min_stack.pop()
assert min_stack.getMin() == -2
