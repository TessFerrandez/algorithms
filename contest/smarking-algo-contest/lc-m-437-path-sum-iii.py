from collections import defaultdict
from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    # brute force
    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> int:
        def test(node, target):
            if not node:
                return
            if node.val == target:
                self.num_paths += 1
            test(node.left, target - node.val)
            test(node.right, target - node.val)

        def dfs(node, target):
            if not node:
                return
            test(node, target)
            dfs(node.left, target)
            dfs(node.right, target)

        self.num_paths = 0
        dfs(root, targetSum)
        return self.num_paths

    # with memoization
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.num_paths = 0
        cache = defaultdict(int)
        cache[0] = 1

        def dfs(root, target, curr_path_sum):
            if not root:
                return

            # calculate current path sum and required old path sum
            curr_path_sum += root.val
            old_path_sum = curr_path_sum - target

            # update results and cache
            self.num_paths += cache[old_path_sum]
            cache[curr_path_sum] = cache[curr_path_sum] + 1

            dfs(root.left, target, curr_path_sum)
            dfs(root.right, target, curr_path_sum)

            # when we move to a new branch, backtrack the current path sum
            cache[curr_path_sum] -= 1

        dfs(root, targetSum, 0)
        return self.num_paths


solution = Solution()
assert solution.pathSum(deserialize([10,5,-3,3,2,None,11,3,-2,None,1]), 8) == 3
assert solution.pathSum(deserialize([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22) == 3
