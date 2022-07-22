from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)

        triplets = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            triplets += 1
        return triplets


solution = Solution()
assert solution.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3) == 4
assert solution.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1) == 0
