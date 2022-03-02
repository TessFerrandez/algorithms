class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        adds = 0

        for ch in s:
            balance += 1 if ch == '(' else -1
            if balance == -1:
                adds += 1
                balance += 1

        return adds + balance


solution = Solution()
assert solution.minAddToMakeValid('())') == 1
assert solution.minAddToMakeValid('(((') == 3
