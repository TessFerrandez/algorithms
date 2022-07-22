from collections import deque
from typing import List, Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        todo = deque([(0, root)])

        while todo:
            level, node = todo.popleft()
            if len(result) <= level:
                result.append(node.val)
            else:
                result[-1] = node.val
            if node.left:
                todo.append((level + 1, node.left))
            if node.right:
                todo.append((level + 1, node.right))

        return result


solution = Solution()
assert solution.rightSideView(deserialize([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
assert solution.rightSideView(deserialize([1, None, 3])) == [1, 3]
assert solution.rightSideView(None) == []
