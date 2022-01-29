from typing import Optional
from TreeNode import TreeNode, create_btree
from collections import deque


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def are_same(root1, root2):
            if root1 is None:
                return root2 is None

            if root2 is None:
                return False

            if root1.val != root2.val:
                return False

            return are_same(root1.left, root2.left) and are_same(root1.right, root2.right)

        if root is None:
            return subRoot is None

        todo = deque([root])
        while todo:
            node = todo.popleft()
            if node.val == subRoot.val:
                if are_same(node, subRoot):
                    return True
            if node.left is not None:
                todo.append(node.left)
            if node.right is not None:
                todo.append(node.right)

        return False


solution = Solution()
print(solution.isSubtree(create_btree([3, 4, 5, 1, 2, None, None, None, None, 0]), create_btree([4, 1, 2])))
print(solution.isSubtree(create_btree([3, 4, 5, 1, 2]), create_btree([4, 1, 2])))
