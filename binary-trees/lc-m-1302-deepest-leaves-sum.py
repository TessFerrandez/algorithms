from collections import deque
from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        current_level, current = 0, []
        todo = deque()
        todo.append((0, root))

        while todo:
            level, node = todo.popleft()
            if level != current_level:
                current.clear()
                current_level = level
            current.append(node.val)
            if node.left:
                todo.append((level + 1, node.left))
            if node.right:
                todo.append((level + 1, node.right))

        return 0 if not current else sum(current)


solution = Solution()
tree = deserialize([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
assert solution.deepestLeavesSum(tree) == 15

tree = deserialize([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5])
assert solution.deepestLeavesSum(tree) == 19
