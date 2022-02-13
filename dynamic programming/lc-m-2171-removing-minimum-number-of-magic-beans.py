'''
You are given an array of positive integers beans, where each integer represents the number of magic beans found in a particular magic bag.

Remove any number of beans (possibly none) from each bag such that the number of beans in each remaining non-empty bag (still containing at least one bean) is equal. Once a bean has been removed from a bag, you are not allowed to return it to any of the bags.

Return the minimum number of magic beans that you have to remove.
'''
from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        if n == 1:
            return 0

        beans.sort()

        total_sum = 0
        bean_sum = []
        for bean in beans:
            total_sum += bean
            bean_sum.append(total_sum)

        best = 10 ** 32
        for i, bean in enumerate(beans):
            curr_sum = 0
            if i > 0:
                curr_sum += bean_sum[i - 1]
            if i < n - 1:
                curr_sum += total_sum - bean_sum[i] - (n - 1 - i) * bean
            best = min(best, curr_sum)

        return best


solution = Solution()
assert solution.minimumRemoval([4, 1, 6, 5]) == 4
assert solution.minimumRemoval([2, 10, 3, 2]) == 7
