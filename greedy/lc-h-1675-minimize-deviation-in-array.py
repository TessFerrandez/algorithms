'''
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.
'''
from typing import List
from heapq import heappush, heappop


class Solution:
    # wrong - cycles
    def minimumDeviation2(self, nums: List[int]) -> int:
        maxn, minn = max(nums), min(nums)
        deviation = maxn - minn

        visited = set()
        visited.add((maxn, minn))

        changed = True
        while changed:
            changed = False
            minn, maxn = min(nums), max(nums)
            if minn % 2 != 0:
                nums.remove(minn)

                new_max = max(maxn, minn * 2)
                new_min = min(min(nums), minn * 2)

                if (new_max - new_min) <= deviation:
                    if deviation == (new_max - new_min) and (new_max, new_min) in visited:
                        return deviation
                    else:
                        deviation = new_max - new_min
                        nums.append(minn * 2)
                        minn, maxn = new_min, new_max
                        visited.add((maxn, minn))
                        changed = True
                else:
                    nums.append(minn)

            if maxn % 2 == 0:
                nums.remove(maxn)
                new_min = min(minn, maxn // 2)
                new_max = max(max(nums), maxn // 2)

                if (new_max - new_min) <= deviation:
                    if deviation == (new_max - new_min) and (new_max, new_min) in visited:
                        return deviation
                    else:
                        deviation = new_max - new_min
                        nums.append(maxn // 2)
                        maxn, minn = new_max, new_min
                        visited.add((maxn, minn))
                        changed = True
                else:
                    nums.append(maxn)

        return deviation

    # TLE
    def minimumDeviation1(self, nums: List[int]) -> int:
        numbers = [num if num % 2 == 0 else num * 2 for num in nums]
        minn, maxn = min(numbers), max(numbers)
        deviation = maxn - minn

        while deviation != 0 and maxn % 2 == 0:
            numbers.remove(maxn)
            numbers.append(maxn // 2)
            minn = min(minn, maxn // 2)
            maxn = max(numbers)
            deviation = min(deviation, maxn - minn)

        return deviation

    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []

        minn = float('inf')
        for num in nums:
            if num % 2 == 0:
                number = num
            else:
                number = 2 * num
            minn = min(minn, number)
            heappush(heap, -number)

        deviation = float('inf')
        while heap:
            maxn = -heappop(heap)
            deviation = min(deviation, maxn - minn)
            if maxn % 2 == 0:
                number = maxn // 2
                minn = min(minn, number)
                heappush(heap, -number)
            else:
                return deviation


solution = Solution()
assert solution.minimumDeviation([2, 8, 6, 1, 6]) == 1
assert solution.minimumDeviation([10, 4, 3]) == 2
assert solution.minimumDeviation([4, 1, 5, 20, 3]) == 3
assert solution.minimumDeviation([1, 2, 3, 4]) == 1
assert solution.minimumDeviation([2, 10, 8]) == 3
