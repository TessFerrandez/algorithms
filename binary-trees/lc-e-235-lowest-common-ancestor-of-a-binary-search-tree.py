'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
from TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowest_common_ancestor(root, min_node, max_node):
            if root == p or root == q:
                return root

            if max_node.val < root.val:
                return lowest_common_ancestor(root.left, min_node, max_node)
            elif min_node.val < root.val < max_node.val:
                return root
            else:
                return lowest_common_ancestor(root.right, min_node, max_node)

        if p.val < q.val:
            min_node = p
            max_node = q
        else:
            min_node = q
            max_node = p

        return lowest_common_ancestor(root, min_node, max_node)


solution = Solution()

head = TreeNode(6)

n2 = TreeNode(2)
n8 = TreeNode(8)
head.left = n2
head.right = n8

n0 = TreeNode(0)
n4 = TreeNode(4)
n2.left = n0
n2.right = n4

n7 = TreeNode(7)
n9 = TreeNode(9)
n8.left = n7
n8.right = n9

n3 = TreeNode(3)
n5 = TreeNode(5)
n4.left = n3
n4.right = n5

assert solution.lowestCommonAncestor(head, n2, n8).val == 6
assert solution.lowestCommonAncestor(head, n2, n4).val == 2
