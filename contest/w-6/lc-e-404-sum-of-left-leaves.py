from typing import Optional
from TreeNode import deserialize, TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_of_left(root, left):
            if not root:
                return 0
            if left and not root.left and not root.right:
                return root.val
            if not root.left and not root.right:
                return 0
            return sum_of_left(root.left, True) + sum_of_left(root.right, False)

        return sum_of_left(root, False)


solution = Solution()
assert solution.sumOfLeftLeaves(deserialize([3, 9, 20, None, None, 15, 7])) == 24
assert solution.sumOfLeftLeaves(deserialize([1])) == 0
