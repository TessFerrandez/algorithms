'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
'''
from TreeNode import TreeNode, deserialize


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def create_bst_from_sorted_array(sorted_array):
            if not sorted_array:
                return None

            low, high = 0, len(sorted_array) - 1
            mid = (low + high) // 2
            root = TreeNode(sorted_array[mid])
            root.left = create_bst_from_sorted_array(sorted_array[:mid])
            root.right = create_bst_from_sorted_array(sorted_array[mid + 1:])
            return root

        def get_sorted_array(root):
            if root is None:
                return []
            return get_sorted_array(root.left) + [root.val] + get_sorted_array(root.right)

        sorted_array = get_sorted_array(root)
        return create_bst_from_sorted_array(sorted_array)


solution = Solution()
root = solution.balanceBST(deserialize([1, None, 2, None, 3, None, 4, None, None]))
