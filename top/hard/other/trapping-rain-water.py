import numpy
from typing import List


class Solution:
    # brute force
    def trap1(self, height: List[int]) -> int:
        answer, n = 0, len(height)

        for i in range(n):
            left_max, right_max = 0, 0
            for j in range(i + 1):
                left_max = max(left_max, height[j])
            for j in range(i, n):
                right_max = max(right_max, height[j])
            answer += min(left_max, right_max) - height[i]

        return answer

    # dp
    def trap2(self, height: List[int]) -> int:
        pre_max = list(numpy.maximum.accumulate(numpy.array(height)))
        post_max = list(numpy.maximum.accumulate(numpy.array(height[::-1])))[::-1]
        return sum(min(pre_max[i], post_max[i]) - height[i] for i in range(len(height)))

    # dp v2
    def trap3(self, height: List[int]) -> int:
        n = len(height)
        trapped = 0

        post_max, maxh = [0] * n, 0
        for i in range(n - 1, -1, -1):
            post_max[i] = maxh = max(maxh, height[i])

        maxh = 0
        for i in range(n):
            maxh = max(maxh, height[i])
            trapped += min(post_max[i], maxh) - height[i]

        return trapped

    # stacks
    def trap(self, height: List[int]) -> int:
        answer, current = 0, 0
        stack = []

        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break

                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                answer += distance * bounded_height

            stack.append(current)
            current += 1

        return answer


solution = Solution()
assert solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert solution.trap([4,2,0,3,2,5]) == 9
