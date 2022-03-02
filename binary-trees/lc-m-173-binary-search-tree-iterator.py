'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
'''
from typing import Optional
from TreeNode import TreeNode, deserialize


class BSTIterator1:
    def __init__(self, root: Optional[TreeNode]):
        self.arr = list(reversed(self.inorder(root)))

    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

    def next(self) -> int:
        return self.arr.pop()

    def hasNext(self) -> bool:
        return self.arr != []


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.smallest = None
        self.dfs(root)

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.right)
        root.right = self.smallest
        self.smallest = root
        self.dfs(root.left)

    def next(self) -> int:
        val = self.smallest.val
        self.smallest = self.smallest.right
        return val

    def hasNext(self) -> bool:
        return self.smallest is not None


iter = BSTIterator(deserialize([7, 3, 15, None, None, 9, 20]))
assert iter.next() == 3
assert iter.next() == 7
assert iter.hasNext()
assert iter.next() == 9
assert iter.hasNext()
assert iter.next() == 15
assert iter.hasNext()
assert iter.next() == 20
assert not iter.hasNext()
