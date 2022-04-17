from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        number of missing at each index are
        0   1   2   3   4
        -------------------
        2   3   4   7   11
        1   1   1   3   6
        == num - index - 1
        '''
        low, high = 0, len(arr)

        while low < high:
            mid = (low + high) // 2
            if arr[mid] - 1 - mid < k:
                low = mid + 1
            else:
                high = mid

        return low + k


solution = Solution()
print(solution.findKthPositive([2, 3, 4, 7, 11], 5))
