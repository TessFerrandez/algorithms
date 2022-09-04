class Solution:
    def countSegments(self, s: str) -> int:
        return sum(1 for part in s.split(' ') if part != '')


solution = Solution()
assert solution.countSegments("Hello, my name is John") == 5
assert solution.countSegments("Hello") == 1
