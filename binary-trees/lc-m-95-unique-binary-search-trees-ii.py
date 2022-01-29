'''
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
'''
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def get_trees(nums: List[int]) -> List[Optional[TreeNode]]:
            if nums == []:
                return [None]

            trees = []
            for i, num in enumerate(nums):
                left_trees = get_trees(nums[:i])
                right_trees = get_trees(nums[i + 1:])
                for left in left_trees:
                    for right in right_trees:
                        trees.append(TreeNode(num, left=left, right=right))

            return trees

        return get_trees(list(range(1, n + 1)))


solution = Solution()
trees = solution.generateTrees(3)
