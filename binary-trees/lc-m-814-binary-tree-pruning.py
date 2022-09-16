from typing import Optional
from TreeNode import TreeNode, deserialize, arr_from_btree


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if not root.left and not root.right and root.val != 1:
            return None

        return root


solution = Solution()
assert arr_from_btree(solution.pruneTree(deserialize([1,None,0,0,1]))) == [1,None,0,None,1]
assert arr_from_btree(solution.pruneTree(deserialize([1,0,1,0,0,0,1]))) == [1,None,1,None,1]
assert arr_from_btree(solution.pruneTree(deserialize([1,1,0,1,1,0,1,0]))) == [1,1,0,1,1,None,1]
