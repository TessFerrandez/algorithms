from typing import List


class Solution:
    def minMaxDistance(self, stations: List[int], k: int) -> int:
        '''
        add k more gas stations so that d (the maximum distance between adjacent gas stations)
        is minimized -- return smallest possible value of d
        '''
        def possible(x, stations, k):
            count = 0
            for i in range(1, len(stations)):
                count += (stations[i] - stations[i - 1]) // x

            return count <= k

        delta = 1e-6
        low, high = 0, 1e8

        while high - low > delta:
            mid = (low + high) / 2
            if possible(mid, stations, k):
                high = mid
            else:
                low = mid

        return low


solution = Solution()
assert round(solution.minMaxDistance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=9), 5) == 0.5
