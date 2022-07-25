from typing import List


class Solution:
    '''
    smaller numbers on right are exactly those that jump during a stable sort
    '''
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enum):
            half = len(enum) // 2

            if half > 0:
                left, right = sort(enum[:half]), sort(enum[half:])

                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


solution = Solution()
assert solution.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
assert solution.countSmaller([-1]) == [0]
assert solution.countSmaller([-1, -1]) == [0, 0]
