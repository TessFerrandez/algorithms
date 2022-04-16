from typing import Optional
from TreeNode import deserialize, TreeNode, arr_from_btree


class Solution:
    def __init__(self) -> None:
        self.total = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root


solution = Solution()
assert arr_from_btree(solution.convertBST(deserialize([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]))) == [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
solution = Solution()
assert arr_from_btree(solution.convertBST(deserialize([0, None, 1]))) == [1, None, 1]
