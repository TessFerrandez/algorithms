from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        preorder_index = 0

        def create_tree(left, right):
            nonlocal preorder_index

            if right < left:
                return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            root.left = create_tree(left, inorder_map[root_value] - 1)
            root.right = create_tree(inorder_map[root_value] + 1, right)
            return root

        return create_tree(0, len(preorder) - 1)


solution = Solution()
assert solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).to_array() == [3, 9, 20, None, None, 15, 7]
assert solution.buildTree([-1], [-1]).to_array() == [-1]
