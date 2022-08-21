from functools import cache


class Solution:
    # too much memory
    def canBeValid1(self, s: str, locked: str) -> bool:
        n = len(s)

        @cache
        def can_do(index, opens):
            if index == n:
                return opens == 0
            if opens < 0:
                return False
            if locked[index] == "1":
                if s[index] == '(':
                    return can_do(index + 1, opens + 1)
                else:
                    return can_do(index + 1, opens - 1)
            else:
                return can_do(index + 1, opens + 1) or can_do(index + 1, opens - 1)

        return can_do(0, 0)

    def canBeValid(self, s: str, locked: str) -> bool:
        # greedily check balance left to right and right to left
        # left to right ensures we have no orphan ')' parentheses
        # right to left ensures we have no orphan '(' parentheses

        # count wild (not locked) characters
        # track the balance for locked parentheses
        #   if balance goes negative, we check if we have enough wild characters to compensate
        # in the end, check that we have enough wild characters to cover positive balance (open parens)

        def validate(s, locked, op):
            balance, wild = 0, 0
            for i in range(len(s)):
                if locked[i] == '1':
                    balance += 1 if s[i] == op else -1
                else:
                    wild += 1
                if wild + balance < 0:
                    return False

            return balance <= wild

        return len(s) % 2 == 0 and validate(s, locked, '(') and validate(s[::-1], locked[::-1], ')')


solution = Solution()
assert solution.canBeValid("))()))", "010100")
assert solution.canBeValid('()()', '0000')
assert not solution.canBeValid(')', '0')
