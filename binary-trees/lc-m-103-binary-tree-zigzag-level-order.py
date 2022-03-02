'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
'''
from typing import List, Optional
from TreeNode import TreeNode, create_btree
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        todo = deque([(0, root)])

        while todo:
            level, node = todo.pop()
            if len(levels) == level:
                levels.append([node.val])
            else:
                levels[level].append(node.val)
            if node.left:
                todo.append((level + 1, node.left))
            if node.right:
                todo.append((level + 1, node.right))

        result = []
        for i in range(len(levels)):
            if i % 2 == 0:
                result.append(list(reversed(levels[i])))
            else:
                result.append(levels[i])
        return result


solution = Solution()
assert solution.zigzagLevelOrder(create_btree([3, 9, 20, None, None, 15, 7])) == [[3], [20, 9], [15, 7]]
assert solution.zigzagLevelOrder(create_btree([1])) == [[1]]
assert solution.zigzagLevelOrder(create_btree([])) == []
