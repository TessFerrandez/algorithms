class Solution:
    # my solution
    def minBitFlips1(self, start: int, goal: int) -> int:
        bstart = '{:032b}'.format(start)
        bgoal = '{:032b}'.format(goal)

        count = 0
        for i in range(len(bstart)):
            if bstart[i] != bgoal[i]:
                count += 1
        return count

    # one liner
    def minBitFlips(self, start: int, goal: int) -> int:
        return (bin(start ^ goal).count('1'))


solution = Solution()
assert solution.minBitFlips(10, 7) == 3
assert solution.minBitFlips(3, 4) == 3
