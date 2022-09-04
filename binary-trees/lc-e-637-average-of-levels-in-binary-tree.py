from collections import deque
from typing import List, Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        todo = deque([(root, 1)])
        levels = [[]]

        while todo:
            node, level = todo.popleft()
            if len(levels) < level:
                levels.append([])
            levels[-1].append(node.val)

            if node.left:
                todo.append((node.left, level + 1))
            if node.right:
                todo.append((node.right, level + 1))

        result = []
        for level in levels:
            result.append(sum(level) / len(level))

        return result


solution = Solution()
assert solution.averageOfLevels(deserialize([3,9,20,None,None,15,7])) == [3.00000,14.50000,11.00000]
assert solution.averageOfLevels(deserialize([3,9,20,15,7])) == [3.00000,14.50000,11.00000]
