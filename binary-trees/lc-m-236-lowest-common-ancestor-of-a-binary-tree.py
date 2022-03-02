'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
from TreeNode import TreeNode, deserialize


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_path(root, node):
            if not root:
                return None

            if root == node:
                return [root]

            left_path = get_path(root.left, node)
            if left_path:
                return [root] + left_path
            right_path = get_path(root.right, node)
            if right_path:
                return [root] + right_path
            return None

        p_path = get_path(root, p)
        q_path = get_path(root, q)

        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            i += 1

        return p_path[i - 1]


solution = Solution()

tree = deserialize([1, 2])
assert solution.lowestCommonAncestor(tree, tree.find(2), tree.find(1)).val == 1

tree = deserialize([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
assert solution.lowestCommonAncestor(tree, tree.find(5), tree.find(1)).val == 3

tree = deserialize([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
assert solution.lowestCommonAncestor(tree, tree.find(5), tree.find(4)).val == 5

tree = deserialize([1, 2])
assert solution.lowestCommonAncestor(tree, tree.find(1), tree.find(2)).val == 1
