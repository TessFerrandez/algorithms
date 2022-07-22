from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def leading_ones(number):
            bin_str = format(number, '08b')
            i = 0
            while i < 8 and bin_str[i] == '1':
                i += 1
            return i

        n = len(data)

        i = 0
        while i < n:
            ones = leading_ones(data[i])
            if ones == 0:
                i += 1
            elif ones == 1:
                return False
            elif ones > 4:
                return False
            else:
                if i + ones > n:
                    return False
                for j in range(1, ones):
                    if leading_ones(data[i + j]) != 1:
                        return False
                i += ones

        return True


solution = Solution()
assert not solution.validUtf8([250,145,145,145,145])
assert not solution.validUtf8([145])
assert not solution.validUtf8([255])
assert solution.validUtf8([197, 130, 1])
assert not solution.validUtf8([235, 140, 4])
