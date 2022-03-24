from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low, high = 0, len(people) - 1

        boats = 0
        while low <= high:
            if people[high] + people[low] <= limit:
                low += 1
            high -= 1
            boats += 1

        return boats


solution = Solution()
assert solution.numRescueBoats([1], 3) == 1
assert solution.numRescueBoats([1,2], 3) == 1
assert solution.numRescueBoats([3,2,2,1], 3) == 3
assert solution.numRescueBoats([3,5,3,4], 5) == 4
