from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        loss = [transaction for transaction in transactions if transaction[0] > transaction[1]]
        earn = [transaction for transaction in transactions if transaction[0] <= transaction[1]]
        loss.sort(key=lambda x: x[1])

        # budget: min required budget
        # current: current budget we have
        budget, current = 0, 0

        for cost, cash_back in loss:
            current -= cost
            budget = min(budget, current)
            current += cash_back

        if earn:
            current -= max(transaction[0] for transaction in earn)
            budget = min(budget, current)

        return -budget


solution = Solution()
assert solution.minimumMoney([[2,1],[5,0],[4,2]]) == 10
assert solution.minimumMoney([[3,0],[0,3]]) == 3
