from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    # brute force TLE
    def countRectangles1(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        result = []

        for x, y in points:
            count = 0
            for length, height in rectangles:
                if x <= length and y <= height:
                    count += 1
            result.append(count)

        return result

    # using binary search and the fact that heights are 1-100
    def countRectangles2(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        def binary_search(arr, x):
            left, right = 0, len(arr) - 1

            # in case we don't find an m such that arr[m] >= x
            # our x is greater than all values
            answers_til_now = len(arr)

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] >= x:
                    answers_til_now = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return answers_til_now

        answers = []

        h_to_l = defaultdict(list)
        for length, height in rectangles:
            h_to_l[height].append(length)

        # sort the lengths to apply binary search
        for _, values in h_to_l.items():
            values.sort()

        for x, y in points:
            count = 0

            for height in range(y, 101):
                if height in h_to_l:
                    count += len(h_to_l[height]) - binary_search(h_to_l[height], x)

            answers.append(count)

        return answers

    # same idea as above but with bisect
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        result = []

        htl = defaultdict(list)
        for length, height in rectangles:
            htl[height].append(length)

        for height in htl:
            htl[height].sort()

        for x, y in points:
            count = 0
            for height in range(y, 101):
                idx = bisect_left(htl[height], x)
                count += len(htl[height]) - idx
            result.append(count)

        return result


solution = Solution()
assert solution.countRectangles([[1,2], [2,3],[2,5]], [[2,1],[1,4]]) == [2, 1]
assert solution.countRectangles([[1,1],[2,2],[3,3]], [[1,3],[1,1]]) == [1, 3]
