'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''
from typing import Optional, List
from TreeNode import TreeNode, deserialize


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        if root is None:
            return []

        if root.val == targetSum and root.left is None and root.right is None:
            return [[root.val]]

        left_paths = self.pathSum(root.left, targetSum - root.val)
        right_paths = self.pathSum(root.right, targetSum - root.val)
        child_paths = left_paths + right_paths
        for path in child_paths:
            paths.append([root.val] + path)

        return paths


solution = Solution()
assert solution.pathSum(deserialize([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]
assert solution.pathSum(deserialize([1, 2, 3]), 5) == []
assert solution.pathSum(deserialize([1, 2]), 0) == []
