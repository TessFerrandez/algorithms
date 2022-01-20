'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

ALGO:
------------------
ex.
A1-A2-C1-C2-C3
B1-B2-B3-C1-C2-C3

First round
p1  p2
A1  B1
A2  B2
C1  B3
C2  C1
C3  C2
B1  C3
B2  A1
B3  A2
C1  C1

So the swap erases the length diff
If we reach the end without matching nodes
we just return the end (None)
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
        return p1
