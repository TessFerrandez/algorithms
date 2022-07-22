from TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = [None]

        def recurse(current):
            if not current:
                return False

            left = recurse(current.left)
            right = recurse(current.right)
            mid = current == p or current == q

            if mid + left + right >= 2:
                answer[0] = current

            return mid or left or right

        # Traverse the tree
        recurse(root)
        return answer[0]


solution = Solution()

p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
q = TreeNode(1, TreeNode(0), TreeNode(8))
tree = TreeNode(3, p, q)
assert solution.lowestCommonAncestor(tree, p, q).val == 3

q = TreeNode(4)
p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), q))
tree = TreeNode(3, p, TreeNode(1, TreeNode(0), TreeNode(8)))
assert solution.lowestCommonAncestor(tree, p, q).val == 5

q = TreeNode(2)
p = TreeNode(1, q)
assert solution.lowestCommonAncestor(p, p, q).val == 1
