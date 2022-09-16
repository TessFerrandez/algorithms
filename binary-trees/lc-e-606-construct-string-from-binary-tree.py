from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def tree2str1(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if left:
            left = f"({left})"
        if right:
            right = f"({right})"
        if right and not left:
            left = "()"

        children = f"{left}{right}" if left or right else ""
        return f"{root.val}{children}"

    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        if not root.left and not root.right:
            return f"{root.val}"
        if not root.right:
            return f"{root.val}({self.tree2str(root.left)})"
        return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"


solution = Solution()
assert solution.tree2str(deserialize([1, 2, 3, 4])) == "1(2(4))(3)"
assert solution.tree2str(deserialize([1,2,3,None,4])) == "1(2()(4))(3)"
