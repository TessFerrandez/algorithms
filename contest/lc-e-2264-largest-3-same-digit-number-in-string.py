class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                best = max(best, int(num[i]))
        return '' if best == -1 else 3 * str(best)


solution = Solution()
assert solution.largestGoodInteger('6777133339') == '777'
assert solution.largestGoodInteger('2300019') == '000'
assert solution.largestGoodInteger('42352338') == ''
