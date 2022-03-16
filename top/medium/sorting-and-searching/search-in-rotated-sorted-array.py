from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_pos = 0
        for i in range(1, n):
            if nums[i] == target:
                return i
            if nums[i] < nums[i - 1]:
                nums = nums[i:] + nums[:i]
                rotate_pos = i
                break

        low, high = 0, n - 1
        while low <= high:
            mid = (high - low) // 2 + low
            if nums[mid] == target:
                return (mid + rotate_pos) % n
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1
