'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
'''
from typing import Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()

        def find_target(node, k):
            if not node:
                return False

            if (k - node.val) in visited:
                return True

            visited.add(node.val)

            return find_target(node.left, k) or find_target(node.right, k)

        return find_target(root, k)


solution = Solution()
assert solution.findTarget(create_btree([5, 3, 6, 2, 4, None, 7]), 9)
