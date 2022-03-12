from typing import Optional
from TreeNode import TreeNode, from_array


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and is_mirror(node1.right, node2.left) and is_mirror(node1.left, node2.right)

        return is_mirror(root, root)


solution = Solution()
assert solution.isSymmetric(from_array([1, 2, 2, 3, 4, 4, 3]))
assert not solution.isSymmetric(from_array([1, 2, 2, None, 3, None, 3]))
