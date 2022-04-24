from typing import Optional
from TreeNode import deserialize, arr_from_btree, TreeNode


class Solution:
    # morris traversal
    def recoverTree1(self, root: Optional[TreeNode]) -> None:
        current, node, candidates = root, TreeNode(-float('inf')), []

        while current:
            if current.left:
                prev = current.left
                while prev.right and prev.right != current:
                    prev = prev.right
                if not prev.right:
                    prev.right = current
                    current = current.left
                else:
                    prev.right = None
                    if current.val < node.val:
                        candidates += [node, current]
                    node = current
                    current = current.right
            else:
                if current.val < node.val:
                    candidates += [node, current]
                node = current
                current = current.right

        candidates[0].val, candidates[-1].val = candidates[-1].val, candidates[0].val

    # inorder traversal
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first, self.second = None, None
        self.prev = TreeNode(-float('inf'))

        def traverse(root):
            if not root:
                return

            traverse(root.left)

            if not self.first and self.prev.val >= root.val:
                self.first = self.prev
            if self.first and self.prev.val >= root.val:
                self.second = root
            self.prev = root

            traverse(root.right)

        traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val


solution = Solution()

tree = deserialize([1, 3, None, None, 2])
solution.recoverTree(tree)
assert arr_from_btree(tree) == [3,1,None,None,2]

tree = deserialize([3, 1, 4, None, None, 2])
solution.recoverTree(tree)
assert arr_from_btree(tree) == [2, 1, 4, None, None, 3]
