class Solution:
    def countSegments(self, s: str) -> int:
        return len([segment for segment in s.split(' ') if segment != ''])


solution = Solution()
assert solution.countSegments("Hello, my name is John") == 5
assert solution.countSegments("Hello") == 1
assert solution.countSegments("Hello  world") == 2
