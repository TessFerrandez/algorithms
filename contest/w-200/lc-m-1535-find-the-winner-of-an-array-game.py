from typing import List


class Solution:
    def getWinner1(self, arr: List[int], k: int) -> int:
        n = len(arr)
        for i in range(len(arr)):
            wins = 0
            if i != 0 and arr[i] > arr[i - 1]:
                wins += 1
            j = (i + 1) % n
            while wins < k and j != i and arr[i] >= arr[j]:
                wins += 1
                j = (j + 1) % n

            if wins == k:
                return arr[i]

        return max(arr)

    # one pass
    def getWinner(self, arr: List[int], k: int) -> int:
        current = arr[0]
        wins = 0

        for i in range(1, len(arr)):
            if arr[i] > current:
                current = arr[i]
                wins = 0
            wins += 1
            if wins == k:
                return current

        return current


solution = Solution()
assert solution.getWinner([2, 1, 3, 5, 4, 6, 7], 2) == 5
assert solution.getWinner([3, 2, 1], 10) == 3
assert solution.getWinner([1,11,22,33,44,55,66,77,88,99], 1000000000) == 99
