from math import inf
from TreeNode import TreeNode, deserialize


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good(node, prev_max):
            if not node:
                return 0

            new_max = max(prev_max, node.val)
            return count_good(node.left, new_max) + (1 if node.val >= prev_max else 0) + count_good(node.right, new_max)

        return count_good(root, -inf)


solution = Solution()
assert solution.goodNodes(deserialize([3,1,4,3,None,1,5])) == 4
assert solution.goodNodes(deserialize([3,3,None,4,2])) == 3
assert solution.goodNodes(deserialize([1])) == 1
