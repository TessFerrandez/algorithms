'''
Given two integer arrays preorder and inorder where preorder is
the preorder traversal of a binary tree and inorder is the inorder
traversal of the same tree, construct and return the binary tree.
'''
from typing import List, Optional
from TreeNode import TreeNode, arr_from_btree


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, num in enumerate(inorder):
            inorder_map[num] = i

        preorder_index = 0

        def array_to_tree(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            root.left = array_to_tree(left, inorder_map[root_value] - 1)
            root.right = array_to_tree(inorder_map[root_value] + 1, right)
            return root

        return array_to_tree(0, len(preorder) - 1)


solution = Solution()
assert arr_from_btree(solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])) == [3, 9, 20, None, None, 15, 7]
assert arr_from_btree(solution.buildTree([-1], [-1])) == [-1]
