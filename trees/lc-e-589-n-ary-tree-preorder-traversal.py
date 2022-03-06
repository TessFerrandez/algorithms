'''
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value
'''
from typing import List


class Node:
    def __init__(self, val=None, children=None) -> None:
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        arr = [root.val]
        if root.children:
            for child in root.children:
                arr += self.preorder(child)
        return arr


solution = Solution()

root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
assert solution.preorder(root) == [1, 3, 5, 6, 2, 4]

root = Node(1, [Node(2),
                Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
                Node(4, [Node(8, [Node(12)])]),
                Node(5, [Node(9, [Node(13)]), Node(10)])])
assert solution.preorder(root) == [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
