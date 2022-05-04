from collections import defaultdict
from typing import Counter, List


class Solution:
    # hashmap O(n) O(n)
    def maxOperations1(self, nums: List[int], k: int) -> int:
        freq = dict(Counter(nums))

        pairs = 0
        for num in freq:
            target = k - num
            if target == num:
                ops = freq[num] // 2
                pairs += ops
                freq[num] -= ops * 2
            elif target > num and target in freq:
                ops = min(freq[num], freq[target])
                pairs += ops
                freq[num] -= ops
                freq[target] -= ops
        return pairs

    # brute force O(n^2) O(1)
    def maxOperations2(self, nums: List[int], k: int) -> int:
        pairs = 0

        for first in range(len(nums)):
            # check if element pointed by first is already "used"
            if nums[first] != 0:
                for second in range(first + 1, len(nums)):
                    # check if the element pointed by second is already "used"
                    if nums[second] != 0 and nums[first] + nums[second] == k:
                        nums[first] = 0
                        nums[second] = 0
                        pairs += 1
                        break

        return pairs

    # sort + two pointer pruning O(n log n) O(1)
    def maxOperations3(self, nums: List[int], k: int) -> int:
        nums.sort()
        pairs, left, right = 0, 0, len(nums) - 1

        while left < right and nums[left] < k:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
                right -= 1
                pairs += 1

        return pairs

    # single pass 2-sum O(n) O(n)
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        pairs = 0

        for num in nums:
            target = k - num
            if freq[target] > 0:
                pairs += 1
                freq[target] -= 1
            else:
                freq[num] += 1

        return pairs


solution = Solution()
assert solution.maxOperations([1, 2, 3, 4], 5) == 2
assert solution.maxOperations([3, 1, 3, 4, 3], 6) == 1
