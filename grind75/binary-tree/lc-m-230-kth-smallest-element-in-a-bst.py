from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        def get_numbers(node):
            if not node:
                return []
            return get_numbers(node.left) + [node.val] + get_numbers(node.right)

        all_numbers = get_numbers(root)
        return all_numbers[k - 1]

    # optimized
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


solution = Solution()
assert solution.kthSmallest(deserialize([3, 1, 4, None, 2]), 1) == 1
assert solution.kthSmallest(deserialize([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
