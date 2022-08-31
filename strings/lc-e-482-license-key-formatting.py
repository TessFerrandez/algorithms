class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(s.split('-')).upper()
        n = len(s)

        result = ''
        i = 0

        if n % k != 0:
            i = n % k
            result = s[: i]

        while i <= n - k:
            result += '-' + s[i: i + k]
            i += k

        if result and result[0] == '-':
            result = result[1:]

        return result


solution = Solution()
assert solution.licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"
assert solution.licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J"
assert solution.licenseKeyFormatting("---", 3) == ""
