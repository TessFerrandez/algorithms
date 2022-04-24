from typing import List


class Solution:
    def trap1(self, height: List[int]) -> int:
        n = len(height)

        prefix_max = [0]
        for h in height:
            prefix_max.append(max(h, prefix_max[-1]))

        trapped = 0
        postfix_max = 0
        for i in range(n - 1, -1, -1):
            if height[i] < min(postfix_max, prefix_max[i]):
                trapped += min(postfix_max, prefix_max[i]) - height[i]
            postfix_max = max(postfix_max, height[i])

        return trapped

    # two pointer
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        trapped = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped += right_max - height[right]

        return trapped


solution = Solution()
assert solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert solution.trap([4,2,0,3,2,5]) == 9
