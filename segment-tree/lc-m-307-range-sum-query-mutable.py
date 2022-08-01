from typing import List


class Node:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray:
    def __init__(self, nums: List[int]):
        def create_tree(nums, left, right):
            if left > right:
                return None
            if left == right:
                node = Node(left, right)
                node.total = nums[left]
                return node

            mid = (left + right) // 2
            root = Node(left, right)
            root.left = create_tree(nums, left, mid)
            root.right = create_tree(nums, mid + 1, right)
            root.total = root.left.total + root.right.total
            return root

        self.root = create_tree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def update_value(root, i, value):
            if root.start == root.end:
                root.total = value
                return value

            mid = (root.start + root.end) // 2

            if i <= mid:
                update_value(root.left, i, value)
            else:
                update_value(root.right, i, value)

            root.total = root.left.total + root.right.total
            return root.total

        return update_value(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def range_sum(root, left, right):
            if root.start == left and root.end == right:
                return root.total
            mid = (root.start + root.end) // 2
            if right <= mid:
                return range_sum(root.left, left, right)
            elif left >= mid + 1:
                return range_sum(root.right, left, right)
            else:
                return range_sum(root.left, left, mid) + range_sum(root.right, mid + 1, right)

        return range_sum(self.root, left, right)


na = NumArray([1, 3, 5])
assert na.sumRange(0, 2) == 9
na.update(1, 2)
assert na.sumRange(0, 2) == 8
