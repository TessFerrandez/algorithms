from typing import Optional
from TreeNode import TreeNode, deserialize
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        levels_min = []
        levels_max = []

        todo = deque([(0, 0, root)])

        while todo:
            level, idx, node = todo.popleft()
            if len(levels_min) > level:
                levels_max[level] = idx
            else:
                levels_min.append(idx)
                levels_max.append(idx)

            if node.left:
                todo.append((level + 1, idx * 2, node.left))
            if node.right:
                todo.append((level + 1, idx * 2 + 1, node.right))

        return max([levels_max[i] - levels_min[i] + 1 for i in range(len(levels_min))])


solution = Solution()
assert solution.widthOfBinaryTree(deserialize([1, 3, 2, 5, 3, None, 9])) == 4
assert solution.widthOfBinaryTree(deserialize([1, 3, None, 5, 3])) == 2
assert solution.widthOfBinaryTree(deserialize([1, 3, 2, 5])) == 2
