from collections import deque
from typing import Optional
from TreeNode import TreeNode, from_array


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 0
        todo = deque([(1, root)])

        while todo:
            depth, node = todo.popleft()
            max_depth = max(depth, max_depth)
            if node.left:
                todo.append((depth + 1, node.left))
            if node.right:
                todo.append((depth + 1, node.right))

        return max_depth


solution = Solution()
assert solution.maxDepth(from_array([3, 9, 20, None, None, 15, 7])) == 3
assert solution.maxDepth(from_array([1, None, 2])) == 2
