from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def exists_in_first(arr, start, element):
            return arr[start] <= element

        def is_binary_search_helpful(arr, left, element):
            return arr[left] != element

        n = len(nums)
        if n == 0:
            return False

        end, start = n - 1, 0
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True

            if not is_binary_search_helpful(nums, start, nums[mid]):
                start += 1
                continue

            pivot_array = exists_in_first(nums, start, nums[mid])
            target_array = exists_in_first(nums, start, target)

            if pivot_array is not target_array:
                if pivot_array:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

        return False


solution = Solution()
assert solution.search([2,5,6,0,0,1,2], 0)
assert not solution.search([2,5,6,0,0,1,2], 3)
