from typing import Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from get_leaves(node.left)
                yield from get_leaves(node.right)

        return list(get_leaves(root1)) == list(get_leaves(root2))


solution = Solution()
assert solution.leafSimilar(create_btree([3,5,1,6,2,9,8,None,None,7,4]), create_btree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]))
assert not solution.leafSimilar(create_btree([1, 2, 3]), create_btree([1, 3, 2]))
