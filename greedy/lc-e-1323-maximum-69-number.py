class Solution:
    def maximum69Number(self, num: int) -> int:
        snum = str(num)
        if '6' in snum:
            i = snum.index('6')
            return int(snum[:i] + '9' + snum[i + 1:])
        return num


solution = Solution()
assert solution.maximum69Number(9669) == 9969
assert solution.maximum69Number(9996) == 9999
assert solution.maximum69Number(9999) == 9999
