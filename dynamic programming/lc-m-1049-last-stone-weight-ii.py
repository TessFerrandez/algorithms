from typing import List


class Solution:
    # knapsack dp solution
    def lastStoneWeightII1(self, stones: List[int]) -> int:
        '''
        all solutions come from combox of sum of (+/-)A(+/-)B(+/-)C...
        ex. - 2 + 7 + 4 + 1 - 8 - 1 = 1 (smallest result)
        so we can turn this into a problem of finding two groups of numbers
        with minimum diff.

        This then becomes a "knapsack problem" i.e. smallest group
        will be the largest group you can fit in sum(stones) // 2
        '''
        all_stones = sum(stones)
        capacity = all_stones // 2
        n = len(stones)

        # this is the sack of "negative" stones
        sack = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for cap_left in range(capacity + 1):
                if i == 0 or cap_left == 0:
                    sack[i][cap_left] = 0
                elif stones[i - 1] <= cap_left:
                    sack[i][cap_left] = max(
                        stones[i - 1] + sack[i - 1][cap_left - stones[i - 1]],
                        sack[i - 1][cap_left]
                    )
                else:
                    sack[i][cap_left] = sack[i - 1][cap_left]

        # we want to return the diff between the positive and negative "sack"
        negative = sack[n][capacity]
        positive = all_stones - negative
        return positive - negative

    # optimized knapsack dp for this problem - using set
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # sum of stones in a group
        sacks = {0}

        # generate all possible stone partitions (or the sum of them)
        for stone in stones:
            sacks |= {sack + stone for sack in sacks}

        # sum(group a) = sum(all) - sum(group b)
        # sum(group a) - sum(group b) = sum(all) - sum(group b) - sum(group b)
        sum_all = sum(stones)
        return min(abs(sum_all - sack - sack) for sack in sacks)


solution = Solution()
assert solution.lastStoneWeightII([2,7,4,1,8,1]) == 1
assert solution.lastStoneWeightII([31,26,33,21,40]) == 5
