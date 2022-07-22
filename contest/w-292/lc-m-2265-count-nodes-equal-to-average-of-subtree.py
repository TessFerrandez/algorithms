from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def get_count(node):
            if node is None:
                return 0, 0, 0
            else:
                left_count, left_sum, left_num = get_count(node.left)
                right_count, right_sum, right_num = get_count(node.right)
                node_sum = left_sum + right_sum + node.val
                node_num = left_num + right_num + 1
                node_avg = node_sum // node_num

                node_count = 1 if node_avg == node.val else 0
                return left_count + right_count + node_count, node_sum, node_num

        count, _, _ = get_count(root)
        return count


solution = Solution()
tree = deserialize([4, 8, 5, 0, 1, None, 6])
assert solution.averageOfSubtree(tree) == 5

tree = deserialize([1])
assert solution.averageOfSubtree(tree) == 1
