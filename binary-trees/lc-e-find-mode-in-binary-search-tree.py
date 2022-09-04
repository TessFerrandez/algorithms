from collections import Counter
from typing import List, Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter()

        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        max_ct = max(count.values())
        return [k for k, v in count.items() if v == max_ct]


solution = Solution()
assert solution.findMode(deserialize([1, None, 2, 2])) == [2]
assert solution.findMode(deserialize([0])) == [0]
