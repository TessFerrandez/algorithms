from bisect import bisect_left, insort
from typing import List


'''
find the number of pairs such that i < j and nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
'''
class Solution:
    # brute force
    def numberOfPairs1(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0

        for i in range(len(nums1)):
            for j in range(i + 1, len(nums2)):
                if nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff:
                    count += 1

        return count

    # short and sweet
    def numberOfPairs2(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0
        diffs = []

        for x, y in zip(nums1, nums2):
            count += len(diffs) - bisect_left(diffs, y - x)
            insort(diffs, y - x + diff)
            print(x, y, diffs)

        return count

    # counting inversions (in merge sort)
    def numberOfPairs3(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        diffs = [nums1[i] - nums2[i] for i in range(n)]
        self.count_i = 0

        def check_count(start, mid, end):
            left, right = start, mid + 1
            while left <= mid and right <= end:
                if diffs[left] <= diffs[right] + diff:
                    self.count_i += end - right + 1
                    left += 1
                else:
                    right += 1

            left, right = start, mid + 1
            temp = []
            while left <= mid and right <= end:
                if diffs[left] <= diffs[right]:
                    temp.append(diffs[left])
                    left += 1
                else:
                    temp.append(diffs[right])
                    right += 1
            while left <= mid:
                temp.append(diffs[left])
                left += 1
            while right <= end:
                temp.append(diffs[right])
                right += 1
            left = start
            for i in range(len(temp)):
                diffs[left + i] = temp[i]

        def merge_sort(start, end):
            if start == end:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid + 1, end)
            check_count(start, mid, end)

        merge_sort(0, n - 1)
        return self.count_i

    # segment tree
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        max_length = 10 ** 6
        tree = [0] * 2 * max_length

        def query_count(right):
            left = max_length
            right += max_length

            result = 0

            while left < right:
                if left & 1:
                    result += tree[left]
                    left += 1
                if right & 1:
                    right -= 1
                    result += tree[right]

                left >>= 1
                right >>= 1

            return result

        def update(index):
            index += max_length
            tree[index] += 1

            while index > 1:
                tree[index >> 1] = tree[index] + tree[index ^ 1]
                index >>= 1

        answer = 0
        for j in range(len(nums1)):
            current_value = nums1[j] - nums2[j]
            current_value += 10 ** 5 + 1    # adding offset to only get positive values
            current_answer = query_count(current_value + 1)
            answer += current_answer
            update(current_value - diff)

        return answer


solution = Solution()
assert solution.numberOfPairs([3, 2, 5], [2, 2, 1], 1) == 3
assert solution.numberOfPairs([3, -1], [-2, 2], -1) == 0
