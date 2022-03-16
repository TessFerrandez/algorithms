from collections import deque
from typing import Optional, List
from TreeNode import TreeNode, from_array


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        todo = deque([(0, root)])

        while todo:
            level, node = todo.popleft()
            if len(result) <= level:
                result.append([node.val])
            else:
                result[level].append(node.val)

            if node.left:
                todo.append((level + 1, node.left))
            if node.right:
                todo.append((level + 1, node.right))

        for i in range(len(result)):
            if i % 2 != 0:
                result[i] = list(reversed(result[i]))

        return result


solution = Solution()
assert solution.zigzagLevelOrder(from_array([3, 9, 20, None, None, 15, 7])) == [[3], [20, 9], [15, 7]]
assert solution.zigzagLevelOrder(from_array([1])) == [[1]]
assert solution.zigzagLevelOrder(from_array([])) == []
