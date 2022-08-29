from collections import defaultdict


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = defaultdict(set)
        for i in range(30):
            pow = str(2 ** i)
            powers[len(pow)].add(pow)

        sorted_n = sorted(str(n))
        for pow in powers[len(sorted_n)]:
            if sorted_n == sorted(str(pow)):
                return True

        return False


solution = Solution()
assert solution.reorderedPowerOf2(1)
assert not solution.reorderedPowerOf2(10)
