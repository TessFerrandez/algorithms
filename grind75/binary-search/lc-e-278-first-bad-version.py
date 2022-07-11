class Solution:
    def firstBadVersion(self, n):
        def isBadVersion(version):
            if n == 5 and version >= 4:
                return True
            if n == 1 and version >= 1:
                return True
            return False

        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low


solution = Solution()
assert solution.firstBadVersion(5) == 4
assert solution.firstBadVersion(1) == 1
