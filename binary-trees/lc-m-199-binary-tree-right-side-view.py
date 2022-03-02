'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''
from typing import Optional, List
from TreeNode import TreeNode, create_btree
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        todo = deque([(0, root)])

        while todo:
            level, node = todo.popleft()

            if node:
                if len(result) > level:
                    result[level] = node.val
                else:
                    # overwrite if we have a more right-most value at that level
                    result.append(node.val)

                todo.append((level + 1, node.left))
                todo.append((level + 1, node.right))

        return result


solution = Solution()
assert solution.rightSideView(create_btree([1, 2, 3, 4])) == [1, 3, 4]
assert solution.rightSideView(create_btree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
assert solution.rightSideView(create_btree([1, None, 3])) == [1, 3]
assert solution.rightSideView(create_btree([])) == []
