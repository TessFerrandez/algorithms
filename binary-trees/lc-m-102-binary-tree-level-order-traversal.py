'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
from typing import List, Optional
from TreeNode import TreeNode, create_btree
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        current_level = -1

        todo = deque([(root, 0)])

        while todo:
            node, level = todo.popleft()

            if node is None:
                continue

            if level != current_level:
                current_level = level
                result.append([node.val])
            else:
                result[-1].append(node.val)

            todo.append((node.left, level + 1))
            todo.append((node.right, level + 1))

        return result


solution = Solution()
assert solution.levelOrder(create_btree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
assert solution.levelOrder(create_btree([1])) == [[1]]
assert solution.levelOrder(create_btree([])) == []
