'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
'''
from typing import Optional
from TreeNode import TreeNode, deserialize, arr_from_btree


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root):
            if not root:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = root.left
            current = root.right
            while current.left:
                current = current.left
            current.left = temp
            return root.right

        if root is None or root.val == key:
            return delete(root)

        current = root
        while current:
            if current.val < key:
                if current.right and current.right.val == key:
                    current.right = delete(current.right)
                    return root
                current = current.right
            else:
                if current.left and current.left.val == key:
                    current.left = delete(current.left)
                    return root
                current = current.left
        return root


solution = Solution()
assert arr_from_btree(solution.deleteNode(deserialize([5, 3, 6, 2, 4, None, 7]), 3)) == [5, 4, 6, 2, None, None, 7]
assert arr_from_btree(solution.deleteNode(deserialize([5, 3, 6, 2, 4, None, 7]), 0)) == [5, 3, 6, 2, 4, None, 7]
assert arr_from_btree(solution.deleteNode(deserialize([]), 0)) == []
