from collections import defaultdict
from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        num_count = defaultdict(int)

        def is_palindrome():
            has_odd = False
            for num in num_count:
                if num_count[num] % 2 == 1:
                    if has_odd:
                        return False
                    has_odd = True
            return True

        def dfs(node):
            num_count[node.val] += 1
            count = 0
            if not node.left and not node.right:
                if is_palindrome():
                    count += 1
            else:
                if node.left:
                    count += dfs(node.left)
                if node.right:
                    count += dfs(node.right)
            num_count[node.val] -= 1
            return count

        count = dfs(root)
        return count


solution = Solution()
assert solution.pseudoPalindromicPaths(deserialize([2,3,1,3,1,None,1])) == 2
assert solution.pseudoPalindromicPaths(deserialize([2,1,1,1,3,None,None,None,None,None,1])) == 1
assert solution.pseudoPalindromicPaths(deserialize([9])) == 1
