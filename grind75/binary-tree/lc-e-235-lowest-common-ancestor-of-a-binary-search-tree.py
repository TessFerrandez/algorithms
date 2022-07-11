from TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        if p.val == root.val or q.val == root.val:
            return root
        elif p.val < root.val and q.val > root.val:
            return root
        elif p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


solution = Solution()

p = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
q = TreeNode(8, TreeNode(7), TreeNode(9))
assert solution.lowestCommonAncestor(TreeNode(6, p, q), p, q).val == 6

q = TreeNode(4, TreeNode(3), TreeNode(5))
p = TreeNode(2, TreeNode(0), q)
assert solution.lowestCommonAncestor(TreeNode(6, p, TreeNode(8, TreeNode(7), TreeNode(9))), p, q).val == 2

q = TreeNode(1)
p = TreeNode(2, q)
assert solution.lowestCommonAncestor(p, p, q).val == 2
