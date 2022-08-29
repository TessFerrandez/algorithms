from typing import List
from sortedcontainers import SortedList


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n, prefix_sums, answer = len(nums), [0], []
        segments, sums = SortedList(), SortedList([0])

        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        def add_segment(left, right):
            segments.add((left, right))
            sums.add(prefix_sums[right + 1] - prefix_sums[left])

        def remove_segment(left, right):
            segments.remove((left, right))
            sums.remove(prefix_sums[right + 1] - prefix_sums[left])

        add_segment(0, n - 1)
        for i in removeQueries:
            # get the index of an interval containing i
            idx = segments.bisect_left((i + 1, - 1)) - 1
            left, right = segments[idx]

            remove_segment(left, right)

            # add the new smaller segments
            if left != i:
                add_segment(left, i - 1)
            if i != right:
                add_segment(i + 1, right)

            answer.append(sums[-1])

        return answer


solution = Solution()
assert solution.maximumSegmentSum([1,2,5,6,1], [0,3,2,4,1]) == [14, 7, 2, 2, 0]
assert solution.maximumSegmentSum([3,2,11,1], [3,2,1,0]) == [16, 5, 3, 0]
