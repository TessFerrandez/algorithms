'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
'''
from typing import List


class Solution:
    # with modification (sort)
    def findDuplicate1(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1

        for num in nums:
            if num == prev:
                return num
            prev = num

        return -1

    # with extra space (set)
    def findDuplicate2(self, nums: List[int]) -> int:
        visited = set()

        for num in nums:
            if num in visited:
                return num
            visited.add(num)

        return -1

    # with modification (negative marking)
    def findDuplicate3(self, nums: List[int]) -> int:
        duplicate = -1

        # negative marking
        for num in nums:
            current = abs(num)
            if nums[current] < 0:
                duplicate = current
                break
            nums[current] *= -1

        # restore numbers
        for i, num in enumerate(nums):
            nums[i] = abs(num)

        return duplicate

    # with modification and recursion (array as hashmap)
    def findDuplicate4(self, nums: List[int]) -> int:
        def store(nums, current):
            if current == nums[current]:
                return current
            next = nums[current]
            nums[current] = current
            return store(nums, next)

        return store(nums, 0)

    # with modification and iterative (array as hashmap)
    def findDuplicate5(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]

    # binary search
    def findDuplicate6(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1

        while low <= high:
            current = (low + high) // 2
            count = 0

            count = sum(num <= current for num in nums)
            if count > current:
                duplicate = current
                high = current - 1
            else:
                low = current + 1

        return duplicate

    # sum of set bits (find the extra positive ones)
    def findDuplicate7(self, nums: List[int]) -> int:
        '''
        sum the bits in all the numbers for 1 -> n
        sum the bits of all the numbers in nums
        set the positive bits to 1 - this is the dupe num (ex. [-1 2 3] = [0 1 1] = 3)
        note 1 << m accesses the mth bit ex 1 << 1 = 001 and 1 << 3 = 100
        to check if mth bit is 1 in num -> if ((1 << m) & num) > 0
            ex (1 << 2) & 12 = 4

        Example run of algo:
        [3 1 3 3 3]

        base_count = (1) [0 0 1], (2) [0 1 1], (3) [0 2 2], (4) [1 2 2]
        nums_count = (3) [0 1 1], (1) [0 1 2], (3) [0 2 3], (3) [0 3 4], (3) [0 4 5]

        [0 4 5] - [1 2 2] = [-1 2 3] => [0 1 1] = 3 if we set all the positives to 1
        '''
        duplicate = 0
        n = len(nums) - 1
        bits = n.bit_length()

        for bit in range(bits):
            mask = 1 << bit
            base_count, nums_count = 0, 0

            for i in range(n + 1):
                # if bit is set in i - add to base count
                if i & mask:
                    base_count += 1

                # if bit is set in nums[i] - add to nums count
                if nums[i] & mask:
                    nums_count += 1

            # if we have more nums than base for this bit
            # set the bit in duplicate
            if nums_count - base_count > 0:
                duplicate |= mask

        return duplicate

    # Tortoise and Hare - find cycle in linked list
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


solution = Solution()
assert solution.findDuplicate([2, 2, 2, 2, 2]) == 2
assert solution.findDuplicate([1, 3, 4, 2, 2]) == 2
assert solution.findDuplicate([3, 1, 3, 4, 2]) == 3
