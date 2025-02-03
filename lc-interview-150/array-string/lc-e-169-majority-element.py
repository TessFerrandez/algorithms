# array, hash table, divide and conquer, sorting, counting
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

    def majorityElement2(self, nums: List[int]) -> int:
        '''
        Boyer Moore Voting Algorithm
        candidate = count = 0
        iterate through array
        if count = 0 then candidate = num
        if num = candidate then count++
        else count--
        '''
        candidate = count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


solution = Solution()
assert(solution.majorityElement([3, 2, 3]) == 3)
assert(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2)

assert(solution.majorityElement2([3, 2, 3]) == 3)
assert(solution.majorityElement2([2, 2, 1, 1, 1, 2, 2]) == 2)
