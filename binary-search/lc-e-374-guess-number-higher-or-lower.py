class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low < high:
            mid = (low + high) // 2
            answer = guess(mid)
            if answer == 0:
                return mid
            elif answer < 0:
                high = mid - 1
            else:
                low = mid + 1

        return low


solution = Solution()
guess = lambda x: -1 if x > 6 else 1 if x < 6 else 0
assert solution.guessNumber(10) == 6

guess = lambda x: -1 if x > 1 else 1 if x < 1 else 0
assert solution.guessNumber(1) == 1
