class Solution:
    # my solution - in contest
    def findNthDigit1(self, n: int) -> int:
        # low, high, digits = 0, 0, 0
        # intervals = []

        # for i in range(1, 10):
        #    first = 10 ** (i - 1)
        #    last = 10 ** (i) - 1
        #    low = high + 1
        #    digits += 1
        #    high = (last - first + 1) * digits + low - 1
        #    intervals.append([first, low, high, digits])

        intervals = [[1, 1, 9, 1], [10, 10, 189, 2], [100, 190, 2889, 3], [1000, 2890, 38889, 4], [10000, 38890, 488889, 5], [100000, 488890, 5888889, 6], [1000000, 5888890, 68888889, 7], [10000000, 68888890, 788888889, 8], [100000000, 788888890, 8888888889, 9]]

        for first, low, high, digits in intervals:
            if n >= low and n <= high:
                n -= low
                number = n // digits
                digit = n % digits
                snum = str(number + first)
                return int(snum[digit])

    # better solution - same idea but more condensed
    def findNthDigit(self, n: int) -> int:
        n -= 1

        for digits in range(1, 11):
            first = 10 ** (digits - 1)
            if n < 9 * first * digits:
                return int(str(first + n // digits)[n % digits])
            n -= 9 * first * digits


solution = Solution()
assert solution.findNthDigit(1000) == 3
assert solution.findNthDigit(3) == 3
assert solution.findNthDigit(11) == 0
assert solution.findNthDigit(191) == 0
