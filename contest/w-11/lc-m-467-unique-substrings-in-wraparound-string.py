class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        def is_consecutive(curr, next):
            return (ord(next) - ord(curr)) % 26 == 1

        result = {ch: 1 for ch in p}
        length = 1

        for i in range(len(p) - 1):
            curr, next = p[i], p[i + 1]
            if is_consecutive(curr, next):
                length += 1
                result[next] = max(result[next], length)
            else:
                length = 1

        return sum(result.values())


solution = Solution()
assert solution.findSubstringInWraproundString('a') == 1
assert solution.findSubstringInWraproundString('cac') == 2
assert solution.findSubstringInWraproundString('zab') == 6
