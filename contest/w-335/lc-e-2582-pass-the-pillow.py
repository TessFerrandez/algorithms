class Solution:
    # my solution
    def passThePillow_my(self, n: int, time: int) -> int:
        diff = 1
        current = 1

        for _ in range(time):
            current += diff
            if current > n:
                current = n - 1
                diff = -1
            elif current == 0:
                current = 2
                diff = 1

        return current

    def passThePillow(self, n: int, time: int) -> int:
        rounds, loc_in_round = divmod(time, n - 1)

        if rounds % 2 == 0:
            return loc_in_round + 1

        return n - loc_in_round


solution = Solution()
assert solution.passThePillow(4, 5) == 2
assert solution.passThePillow(3, 2) == 3
