class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.max_size = k
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.tail = (self.tail + 1) % self.max_size
        self.data[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head, self.tail = 0, -1
        else:
            self.head = (self.head + 1) % self.max_size

        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.tail == -1

    def isFull(self) -> bool:
        return not self.isEmpty() and (self.tail + 1) % self.max_size == self.head


queue = MyCircularQueue(3)
assert queue.enQueue(1)
assert queue.enQueue(2)
assert queue.enQueue(3)
assert not queue.enQueue(4)
assert queue.Rear() == 3
assert queue.isFull()
assert queue.deQueue()
assert queue.enQueue(4)
assert queue.Rear() == 4
