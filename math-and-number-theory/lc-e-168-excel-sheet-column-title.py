class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''

        while columnNumber > 0:
            result = chr(ord('A') + (columnNumber - 1) % 26) + result
            columnNumber = (columnNumber - 1) // 26

        return result


solution = Solution()
assert solution.convertToTitle(1) == 'A'
assert solution.convertToTitle(28) == 'AB'
assert solution.convertToTitle(701) == 'ZY'
