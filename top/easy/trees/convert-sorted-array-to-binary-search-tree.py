from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


solution = Solution()
assert solution.sortedArrayToBST([-10, -3, 0, 5, 9]).to_array() == [0, -3, 9, -10, None, 5]
assert solution.sortedArrayToBST([1, 3]).to_array() == [3, 1]
