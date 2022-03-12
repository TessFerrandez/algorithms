from collections import deque
from typing import Optional, List
from TreeNode import TreeNode, from_array


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        todo = deque([(0, root)])

        result = []

        while todo:
            level, node = todo.popleft()
            if len(result) == level:
                result.append([node.val])
            else:
                result[level].append(node.val)

            if node.left:
                todo.append((level + 1, node.left))
            if node.right:
                todo.append((level + 1, node.right))

        return result


solution = Solution()
assert solution.levelOrder(from_array([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
assert solution.levelOrder(from_array([1])) == [[1]]
assert solution.levelOrder(None) == []
