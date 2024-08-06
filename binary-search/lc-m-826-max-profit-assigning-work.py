from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        # sort the job profile based on difficulty - with max profit to that difficulty
        job_profile = list(sorted(zip(difficulty, profit)))
        max_profit = 0

        job_profile_max_profit = []
        for difficulty, profit in job_profile:
            max_profit = max(max_profit, profit)
            job_profile_max_profit.append((difficulty, max_profit))

        # binary search for the max profit for the given ability
        net_profit = 0

        for ability in worker:
            left, right = 0, len(job_profile_max_profit) - 1
            job_profit = 0

            while left <= right:
                mid = (left + right) // 2
                if job_profile_max_profit[mid][0] <= ability:
                    job_profit = max(job_profit, job_profile_max_profit[mid][1])
                    left = mid + 1
                else:
                    right = mid - 1

            net_profit += job_profit

        return net_profit


solution = Solution()
assert solution.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]) == 0
assert solution.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]) == 100
