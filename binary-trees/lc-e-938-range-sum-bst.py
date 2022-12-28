from typing import Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


solution = Solution()
assert solution.rangeSumBST(create_btree([10,5,15,3,7,None,18]), 7, 15) == 32
assert solution.rangeSumBST(create_btree([10,5,15,3,7,13,18,1,None,6]), 6, 10) == 23
