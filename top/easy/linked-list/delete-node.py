from ListNode import ListNode


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


solution = Solution()

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
solution.deleteNode(head.next)
assert head.to_arr() == [4, 1, 9]

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
solution.deleteNode(head.next.next)
assert head.to_arr() == [4, 5, 9]
