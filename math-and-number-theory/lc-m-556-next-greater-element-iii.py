class Solution:
    def nextGreaterElement(self, n: int) -> int:
        ''' See https://leetcode.com/problems/next-greater-element-iii/discuss/983076/Python-O(m)-solution-explained '''
        digits = list(str(n))
        i = len(digits) - 1

        while i - 1 >= 0 and digits[i] <= digits[i - 1]:
            i -= 1

        if i == 0:
            return -1

        j = i
        while j + 1 < len(digits) and digits[j + 1] > digits[i - 1]:
            j += 1

        digits[i - 1], digits[j] = digits[j], digits[i - 1]
        digits[i:] = digits[i:][::-1]
        result = int(''.join(digits))

        return result if result < 1 << 31 else -1


solution = Solution()
assert solution.nextGreaterElement(12) == 21
assert solution.nextGreaterElement(21) == -1
