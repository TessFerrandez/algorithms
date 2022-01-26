'''
Given two binary search trees root1 and root2,
return a list containing all the integers from both trees sorted in ascending order.
'''
from typing import List, Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def get_elements(tree):
            if tree is None or tree.val is None:
                return []
            return get_elements(tree.left) + [tree.val] + get_elements(tree.right)

        return sorted(get_elements(root1) + get_elements(root2))


solution = Solution()
tree1, tree2 = create_btree([2, 1, 4]), create_btree([1, 0, 3])
assert solution.getAllElements(tree1, tree2) == [0, 1, 1, 2, 3, 4]

tree1, tree2 = create_btree([1, None, 8]), create_btree([8, 1])
assert solution.getAllElements(tree1, tree2) == [1, 1, 8, 8]
