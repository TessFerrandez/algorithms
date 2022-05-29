class Solution:
    def digitCount(self, num: str) -> bool:
        for digit, count in enumerate(num):
            if num.count(str(digit)) != int(count):
                return False
        return True


solution = Solution()
assert solution.digitCount('1210')
assert not solution.digitCount('030')
