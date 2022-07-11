from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(node):
            if not node:
                return True, 0
            left_balanced, left_height = is_balanced(node.left)
            right_balanced, right_height = is_balanced(node.right)
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = is_balanced(root)
        return balanced


solution = Solution()
assert solution.isBalanced(deserialize([3,9,20,None,None,15,7]))
assert not solution.isBalanced(deserialize([1,2,2,3,3,None,None,4,4]))
assert solution.isBalanced(None)
