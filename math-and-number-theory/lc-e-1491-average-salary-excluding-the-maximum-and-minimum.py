'''
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
'''
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary) - min(salary) - max(salary)
        return total / (len(salary) - 2)


solution = Solution()
assert solution.average([4000, 3000, 1000, 2000]) == 2500
assert solution.average([1000, 2000, 3000]) == 2000
