from typing import List


class Solution:
    # with extra space
    def firstMissingPositive1(self, nums: List[int]) -> int:
        nset = set(nums)
        i = 1
        while i in nset:
            i += 1
        return i

    # my solution - pidgeon holes
    def firstMissingPositive2(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)

        def swap(number):
            if 0 <= number < n and nums[number] != number:
                next = nums[number]
                nums[number] = number
                swap(next)

        for i in range(n):
            current = nums[i]
            if current != i:
                nums[i] = 0
                swap(current)

        for i in range(1, n):
            if nums[i] == 0:
                return i

        return n

    # similar idea but iterative
    def firstMissingPositive3(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)

        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0

        for i in range(n):
            nums[nums[i] % n] += n

        print(nums)
        for i in range(n):
            if nums[i] // n == 0:
                return i

        return n

    # similar idea but iterative
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)

        for i in range(n):
            while 0 <= nums[i] < n and nums[nums[i]] != nums[i]:
                tmp = nums[i]
                nums[i], nums[tmp] = nums[tmp], nums[i]

        for i in range(n):
            if nums[i] != i:
                return i

        return n


solution = Solution()
assert solution.firstMissingPositive([2]) == 1
assert solution.firstMissingPositive([1]) == 2
assert solution.firstMissingPositive([1, 2, 0]) == 3
assert solution.firstMissingPositive([3, 4, -1, 1]) == 2
assert solution.firstMissingPositive([7, 8, 9, 11, 12]) == 1
