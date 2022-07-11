class Solution:
    def isValid(self, s: str) -> bool:
        closing = {'}':'{', ']':'[', ')':'('}
        remaining = []

        for ch in s:
            if ch in closing:
                if remaining and remaining[-1] == closing[ch]:
                    remaining.pop()
                else:
                    return False
            else:
                remaining.append(ch)

        return not remaining


solution = Solution()
assert solution.isValid('()')
assert solution.isValid('()[]{}')
assert not solution.isValid('(]')
