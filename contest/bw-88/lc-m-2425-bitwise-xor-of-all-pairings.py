from typing import List


class Solution:
    # my solution during competition
    def xorAllNums1(self, nums1: List[int], nums2: List[int]) -> int:
        ones = [0] * 32
        total_nums2 = len(nums2)

        best = 32
        for num in nums2:
            i = 31
            while num:
                if num & 1:
                    ones[i] += 1
                i -= 1
                num >>= 1
            best = min(best, i)

        result = [0] * 32

        for num in nums1:
            i = 31
            while num:
                if num & 1:
                    result[i] += total_nums2 - ones[i]
                else:
                    result[i] += ones[i]
                i -= 1
                num >>= 1

            while i >= best:
                result[i] += ones[i]
                i -= 1

        val = ''
        for digit in result:
            if digit % 2 == 0:
                val += '0'
            else:
                val += '1'

        return int(val, 2)

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Ex. Both arrays are even
        nums1 = A, B
        nums2 = C, D
        xor = A^C^A^D^B^C^B^D => 0 (since the As cancel each other out, so do the Bs etc. (even cancels out))

        Ex. Both arrays are odd
        nums1 = A, B, C
        nums2 = D, E, F
        xor = A^D^A^E^A^F^B^D^B^E^B^F^C^D^C^E^C^F => A^B^C^D^E^F

        Ex. nums1 is odd
        nums1 = A, B, C
        nums2 = D, E
        xor = A^D^A^E^B^D^B^E^C^D^C^E => D^E

        Ex. nums2 is odd
        nums1 = A, B
        nums2 = C, D, E
        xor = A^C^A^D^A^E^B^C^B^D^B^E => A^B
        '''
        xor1, xor2 = 0, 0
        n1_even, n2_even = len(nums1) % 2 == 0, len(nums2) % 2 == 0

        if n1_even and n2_even:
            return 0

        for num in nums1:
            xor1 ^= num

        for num in nums2:
            xor2 ^= num

        if n1_even:
            return xor1

        if n2_even:
            return xor2

        return xor1 ^ xor2


solution = Solution()
assert solution.xorAllNums([2, 1, 3], [10, 2, 5, 0]) == 13
assert solution.xorAllNums([1, 2], [3, 4]) == 0
