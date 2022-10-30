from typing import List


class Solution:
    def findContentChildren(self, greed: List[int], sizes: List[int]) -> int:
        greed.sort()
        sizes.sort(reverse=True)

        content = 0

        for child_greed in greed:
            while sizes and sizes[-1] < child_greed:
                sizes.pop()

            if not sizes:
                break

            sizes.pop()
            content += 1

        return content


solution = Solution()
assert solution.findContentChildren([1,2,3], [1,1]) == 1
assert solution.findContentChildren([1,2], [1,2,3]) == 2
