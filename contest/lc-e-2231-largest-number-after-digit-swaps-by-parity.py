class Solution:
    # my contest solution
    def largestInteger1(self, num: int) -> int:
        snum = str(num)
        digits = [int(ch) for ch in snum]

        evens, even_is = [], []
        odds, odd_is = [], []
        for i, digit in enumerate(digits):
            if digit % 2 == 1:
                odds.append(digit)
                odd_is.append(i)
            else:
                evens.append(digit)
                even_is.append(i)

        odds.sort(reverse=True)
        evens.sort(reverse=True)

        result = [0] * len(snum)
        for i, idx in enumerate(even_is):
            result[idx] = str(evens[i])
        for i, idx in enumerate(odd_is):
            result[idx] = str(odds[i])

        return int(''.join(result))

    # cleanup
    def largestInteger(self, num: int) -> int:
        digits = [int(c) for c in str(num)]

        evens = sorted([d for d in digits if d % 2 == 0])
        odds = sorted([d for d in digits if d % 2 == 1])

        result = 0
        for d in digits:
            result *= 10
            if d % 2 == 0:
                result += evens.pop()
            else:
                result += odds.pop()

        return result


solution = Solution()
assert solution.largestInteger(1234) == 3412
assert solution.largestInteger(65875) == 87655
