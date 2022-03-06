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

    def findTarget2(self, root: Optional[TreeNode], k: int) -> bool:
        def serialize(root):
            if root is None:
                return []
            return serialize(root.left) + [root.val] + serialize(root.right)

        nums = serialize(root)
        for i, num in enumerate(nums):
            target = k - num
            if target in nums[i + 1:]:
                return True

        return False


solution = Solution()
assert solution.findTarget(create_btree([5, 3, 6, 2, 4, None, 7]), 9)
