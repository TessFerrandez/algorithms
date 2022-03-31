class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def flip_mid(s):
            mid = len(s) // 2
            bit = '1' if s[mid] == '0' else '0'
            result = s[:mid] + bit + s[mid + 1:]
            return result

        current = '0'
        for _ in range(1, n):
            current = current + '1' + flip_mid(current)

        return current[k - 1]


solution = Solution()
assert solution.findKthBit(3, 1) == '0'
assert solution.findKthBit(4, 11) == '1'
