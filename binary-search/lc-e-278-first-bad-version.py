class Solution:
    def firstBadVersion1(self, n):
        lower = 1
        upper = n

        while upper != lower:
            current = lower + ((upper - lower) // 2)
            if isBadVersion(current):
                upper = current
            else:
                lower = current + 1

        return upper

    # template
    def firstBadVersion(self, n):

        low, high = 1, n

        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low


solution = Solution()

isBadVersion = lambda version: version >= 1
assert solution.firstBadVersion(5) == 1

isBadVersion = lambda version: version >= 4
assert solution.firstBadVersion(5) == 4
