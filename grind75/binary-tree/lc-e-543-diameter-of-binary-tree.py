from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_depth(node, diameter):
            if not node:
                return 0
            left, right = max_depth(node.left, diameter), max_depth(node.right, diameter)
            diameter[0] = max(diameter[0], left + right)
            return 1 + max(left, right)

        diameter = [0]
        max_depth(root, diameter)
        return diameter[0]


solution = Solution()
assert solution.diameterOfBinaryTree(deserialize([1, 2, 3, 4, 5])) == 3
assert solution.diameterOfBinaryTree(deserialize([1, 2])) == 1
