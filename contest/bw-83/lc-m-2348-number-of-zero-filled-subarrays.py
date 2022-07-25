from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        prev = -2

        count = 0
        counts = []
        for i in range(len(nums)):
            if nums[i] == 0:
                if i == prev + 1:
                    count += 1
                else:
                    count = 1
                prev = i
            else:
                if count > 0:
                    counts.append(count)
                    count = 0
        if count != 0:
            counts.append(count)

        total = 0
        for count in counts:
            total += (count * (count + 1)) // 2

        return total


solution = Solution()
print(solution.zeroFilledSubarray([1,3,0,0,2,0,0,4]))
print(solution.zeroFilledSubarray([0,0,0,2,0,0]))
print(solution.zeroFilledSubarray([2,10,2019]))
