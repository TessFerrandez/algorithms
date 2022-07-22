from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total = 0

        prev = 0
        for upper, percent in brackets:
            amount = upper - prev
            if upper > income:
                amount = income - prev
            total += (amount * percent) / 100
            if upper > income:
                break
            else:
                prev = upper
        return total


solution = Solution()
assert solution.calculateTax([[3,50],[7,10],[12,25]], 10) == 2.65
assert solution.calculateTax([[1,0],[4,25],[5,50]], 2) == 0.25
assert solution.calculateTax([[2, 50]], 0) == 0.0
