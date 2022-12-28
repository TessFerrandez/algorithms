from typing import Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, min_val, max_val):
            if not root:
                return max_val - min_val
            max_val = max(max_val, root.val)
            min_val = min(min_val, root.val)
            return max(dfs(root.left, min_val, max_val), dfs(root.right, min_val, max_val))

        return dfs(root, root.val, root.val)


solution = Solution()
assert solution.maxAncestorDiff(create_btree([8,3,10,1,6,None,14,None,None,4,7,13])) == 7
assert solution.maxAncestorDiff(create_btree([1, None, 2, None, 0, 3])) == 3
