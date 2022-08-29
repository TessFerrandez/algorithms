from collections import defaultdict
from itertools import accumulate
from typing import List


class SegmentTreeNode:
    def __init__(self, low, high) -> None:
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.count = 0


class Solution:
    # prefix sum and hashmap O(n * (upper - lower))
    def countRangeSum1(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = [0] + list(accumulate(nums))
        record = defaultdict(int)

        result = 0
        for psum in prefix_sum:
            for target in range(lower, upper + 1):
                if psum - target in record:
                    result += record[psum - target]
            record[psum] += 1

        return result

    # prefix sum and segment tree O(log n)
    def countRangeSum2(self, nums: List[int], lower: int, upper: int) -> int:
        def _build(left, right):
            root = SegmentTreeNode(prefix_sum[left], prefix_sum[right])
            if left == right:
                return root

            mid = (left + right) // 2
            root.left = _build(left, mid)
            root.right = _build(mid + 1, right)
            return root

        def _update(root, val):
            if not root:
                return
            if root.low <= val <= root.high:
                root.count += 1
                _update(root.left, val)
                _update(root.right, val)

        def _query(root, lower, upper):
            if lower <= root.low and root.high <= upper:
                return root.count
            if upper < root.low or root.high < lower:
                return 0
            return _query(root.left, lower, upper) + _query(root.right, lower, upper)

        prefix_sum = sorted([0] + list(accumulate(nums)))
        root = _build(0, len(prefix_sum) - 1)

        result = 0
        for prefix in prefix_sum:
            result += _query(root, prefix - upper, prefix - lower)
            _update(root, prefix)

        return result

    # prefix + merge sort O(n log n)
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = [0] + list(accumulate(nums))

        # inclusive
        def merge_sort(left, right):
            if left == right:
                return 0
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)

            i = j = mid + 1

            # O(n)
            for left_most in prefix_sum[left: mid + 1]:
                while i <= right and prefix_sum[i] - left_most < lower:
                    i += 1
                while j <= right and prefix_sum[j] - left_most <= upper:
                    j += 1
                count += j - i

            prefix_sum[left: right + 1] = sorted(prefix_sum[left: right + 1])
            return count

        return merge_sort(0, len(prefix_sum) - 1)


solution = Solution()
assert solution.countRangeSum([-2, 5, -1], -2, 2) == 3
assert solution.countRangeSum([0], 0, 0) == 1
