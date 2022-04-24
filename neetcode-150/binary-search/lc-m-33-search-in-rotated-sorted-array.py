from typing import List


class Solution:
    # my solution
    def search1(self, nums: List[int], target: int) -> int:
        def find_pivot():
            left, right = 0, len(nums) - 1

            if right == left:
                return left

            while left <= right:
                mid = (left + right) // 2
                if mid < right and nums[mid] > nums[mid + 1]:
                    return mid
                if mid > left and nums[mid] < nums[mid - 1]:
                    return mid - 1

                if nums[left] >= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return len(nums) - 1

        def search_normal():
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return -1

        pivot = find_pivot()
        nums = nums[pivot + 1:] + nums[:pivot + 1]
        i = search_normal()
        if i == -1:
            return -1
        return (i + pivot + 1) % len(nums)

    # clever - setting those on the "wong side" to inf or -inf
    def search2(self, nums: List[int], target: int) -> int:
        '''
        ex. search for 14 in [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        but think of the array as [12, 13, 14, 15, 16, 17, 18, 19, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
        likewise, if you search for something between 0-1 then 12-20 are -INF
        '''
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) // 2

            correct_side = ((nums[mid] < nums[0]) == (target < nums[0]))
            if correct_side:
                num = nums[mid]
            else:
                if target < nums[0]:
                    num = -float('inf')
                else:
                    num = float('inf')

            if num < target:
                low = mid + 1
            elif num > target:
                high = mid
            else:
                return mid

        return -1

    # clever simplified
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) // 2
            if target < nums[0] < nums[mid]:        # -inf side
                low = mid + 1
            elif target >= nums[0] > nums[mid]:     # +inf side
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                return mid

        return -1


solution = Solution()
assert solution.search([4, 5, 6, 7, 0, 1, 2, 3], 0) == 4
assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
