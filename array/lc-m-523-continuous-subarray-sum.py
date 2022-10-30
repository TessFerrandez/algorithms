from typing import List


class Solution:
    # TLE
    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        visited = set()
        visited.add(nums[0] % k)

        for num in nums[1:]:
            new_visited = set()
            for prev in visited:
                prev_sum = (prev + num) % k
                if prev_sum == 0:
                    return True
                new_visited.add(prev_sum)
            new_visited.add(num % k)
            visited = new_visited

        return False

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        ex.         -1  0   1   2   3   4
                    ----------------------
                        23  2   4   6   7       k = 6
                    ----------------------
        prefix      0   23  25  29  35  42
        remainder   0   5   1   5               we saw this remainder at 0 so len == 2 - 0 = 2
        '''
        # last index for this remainder
        remainder_index = {0: -1}
        prefix_remainder = 0

        for i in range(len(nums)):
            prefix_remainder = (prefix_remainder + nums[i]) % k

            if prefix_remainder not in remainder_index:
                remainder_index[prefix_remainder] = i
            elif (i - remainder_index[prefix_remainder]) >= 2:
                return True

        return False


solution = Solution()
assert solution.checkSubarraySum([23,2,4,6,7], 6)
assert solution.checkSubarraySum([23,2,6,4,7], 6)
assert not solution.checkSubarraySum([23, 2, 6, 4, 7], 13)
