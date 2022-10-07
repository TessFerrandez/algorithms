from typing import Optional
from TreeNode import TreeNode, deserialize, arr_from_btree


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        depth_nodes = [root]

        for _ in range(2, depth):
            new_nodes = []
            for node in depth_nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            depth_nodes = new_nodes

        for node in depth_nodes:
            left, right = node.left, node.right
            node.left = TreeNode(val, left, None)
            node.right = TreeNode(val, None, right)

        return root


solution = Solution()
assert arr_from_btree(solution.addOneRow(deserialize([4, 2, 6, 3, 1, 5]), 1, 2)) == [4, 1, 1, 2, None, None, 6, 3, 1, 5]
assert arr_from_btree(solution.addOneRow(deserialize([4, 2, None, 3, 1]), 1, 3)) == [4, 2, None, 1, 1, 3, None, None, 1]
assert arr_from_btree(solution.addOneRow(deserialize([4,2,6,3,1,5]), 1, 1)) == [1,4,None,2,6,3,1,5]
