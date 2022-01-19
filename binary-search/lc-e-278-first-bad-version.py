def isBadVersion(version):
    return version >= 1


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        upper = n

        while upper != lower:
            current = lower + ((upper - lower) // 2)
            if isBadVersion(current):
                upper = current
            else:
                lower = current + 1

        return upper

solution = Solution()
print(solution.firstBadVersion(5))
