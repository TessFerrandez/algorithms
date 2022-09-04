from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poison_days = 0
        last_poison = -1

        for attack_day in timeSeries:
            if attack_day <= last_poison:
                overlap_days = last_poison - attack_day + 1
            else:
                overlap_days = 0
            poison_days += duration - overlap_days
            last_poison = attack_day + duration - 1

        return poison_days


solution = Solution()
assert solution.findPoisonedDuration([1, 4], 2) == 4
assert solution.findPoisonedDuration([1, 2], 2) == 3
