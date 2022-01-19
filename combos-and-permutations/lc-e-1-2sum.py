'''
Given a list of numbers and a target number, find out the index of
the two numbers that sum up to the target - in < O(n2)

Hints:
1. Brute force is good for finding optimizations
2. If we fix one number (x) then we have to scan the array to find
   (y) which is (target - x) - can we change the array so this search
   is faster?
3. Can we use more space to make the lookup faster? maybe a hashmap/dict?
'''
from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(list)
        for index, num in enumerate(nums):
            num_dict[num].append(index)

        for num in nums:
            needed = target - num
            if needed in num_dict:
                if needed == num:
                    if len(num_dict[num]) == 2:
                        return num_dict[num]
                else:
                    return [num_dict[num][0], num_dict[needed][0]]


solution = Solution()
assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert solution.twoSum([3, 2, 4], 6) == [1, 2]
assert solution.twoSum([3, 3], 6) == [0, 1]
