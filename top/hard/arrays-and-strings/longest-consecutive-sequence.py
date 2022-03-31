from typing import List


class Solution:
    # O(NlogN)
    def longestConsecutive1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        prev = -10 ** 10

        count = 1
        max_count = 1

        for num in nums:
            if num == prev:
                pass
            elif num == prev + 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
            prev = num

        max_count = max(max_count, count)
        return max_count

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


solution = Solution()
assert solution.longestConsecutive([]) == 0
assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
