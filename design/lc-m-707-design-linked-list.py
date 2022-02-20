class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = ListNode()

    def get(self, index: int) -> int:
        if index >= self.count:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        if self.count == 0:
            self.head.val = val
        else:
            node = ListNode(val, self.head)
            self.head = node

        self.count += 1

    def addAtTail(self, val: int) -> None:
        if self.count == 0:
            self.addAtHead(val)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = ListNode(val)
            self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.count:
            self.addAtTail(val)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node = ListNode(val, current.next)
            current.next = node
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next

            node = current.next
            if index == self.count - 1:
                current.next = None
                del node
            else:
                current.next = node.next
                del node
        self.count -= 1


ll = MyLinkedList()
ll.addAtIndex(0, 10)
ll.addAtIndex(0, 20)
ll.addAtIndex(1, 30)
print(ll.get(0))

ll = MyLinkedList()
ll.addAtHead(7)
ll.addAtHead(2)
ll.addAtHead(1)
ll.addAtIndex(3, 0)
ll.deleteAtIndex(2)
ll.addAtHead(6)
ll.addAtTail(4)
print(ll.get(4))
ll.addAtHead(4)
ll.addAtIndex(5, 0)
ll.addAtHead(6)

ll = MyLinkedList()
ll.addAtHead(1)
ll.deleteAtIndex(0)

ll = MyLinkedList()
ll.addAtHead(1)
ll.addAtTail(3)
ll.addAtIndex(1, 2)
print(ll.get(1))
ll.deleteAtIndex(1)
print(ll.get(1))
print(ll.get(2))
