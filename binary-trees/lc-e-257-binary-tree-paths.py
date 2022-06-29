from typing import List, Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        lefts = self.binaryTreePaths(root.left)
        rights = self.binaryTreePaths(root.right)
        children = lefts + rights

        if not children:
            return [f"{root.val}"]

        result = []
        for child in children:
            result.append(f"{root.val}->{child}")

        return result


solution = Solution()
assert solution.binaryTreePaths(create_btree([1, 2, 3, None, 5])) == ["1->2->5", "1->3"]
assert solution.binaryTreePaths(create_btree([1])) == ["1"]
