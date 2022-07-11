from collections import deque
from typing import List, Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        todo = deque([(root, 0)])

        result = []
        while todo:
            node, level = todo.popleft()
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)

            if node.left:
                todo.append((node.left, level + 1))
            if node.right:
                todo.append((node.right, level + 1))

        return result


solution = Solution()
assert solution.levelOrder(deserialize([3,9,20,None,None,15,7])) == [[3],[9,20],[15,7]]
assert solution.levelOrder(deserialize([1])) == [[1]]
assert solution.levelOrder(None) == []
