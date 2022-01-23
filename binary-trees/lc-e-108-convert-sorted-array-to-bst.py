from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        low, high = 0, len(nums) - 1

        mid = (high - low) // 2 + low
        head = TreeNode(nums[mid])

        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid + 1:])
        return head