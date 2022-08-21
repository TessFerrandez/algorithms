class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs


solution = Solution()
assert solution.poorPigs(1000, 15, 60) == 5
assert solution.poorPigs(4, 15, 15) == 2
assert solution.poorPigs(4, 15, 30) == 2
