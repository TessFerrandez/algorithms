from typing import Optional
from TreeNode import deserialize, TreeNode, arr_from_btree


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val > high:
            return self.trimBST(root.left, low, high)

        if root.val < low:
            return self.trimBST(root.right, low, high)

        root.right = self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)
        return root


solution = Solution()
assert arr_from_btree(solution.trimBST(deserialize([1, 0, 2]), 1, 2)) == [1, None, 2]
assert arr_from_btree(solution.trimBST(deserialize([3, 0, 4, None, 2, None, None, 1]), 1, 3)) == [3, 2, None, 1]
