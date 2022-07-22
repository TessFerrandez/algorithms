class Solution:
    # my solution - brute force
    def removeDigit1(self, number: str, digit: str) -> str:
        max_val, best = 0, ''
        for i in range(len(number)):
            if number[i] == digit:
                num = int(number[:i] + number[i + 1:])
                if num > max_val:
                    max_val = num
                    best = num

        return str(best)

    # remove the leftmost digit that has a following digit
    # that is larger (or last)
    def removeDigit(self, number: str, digit: str) -> str:
        '''
        Ex. 1323413 (pick 3)
        123413
        132413 <-
        132341
        '''
        idx, n = 0, len(number)
        for i in range(n):
            if number[i] == digit:
                idx = i
                if i < n - 1 and digit < number[i + 1]:
                    break
        return number[:idx] + number[idx + 1:]


solution = Solution()
assert solution.removeDigit('123', '3') == '12'
assert solution.removeDigit('1231', '1') == '231'
assert solution.removeDigit('551', '5') == '51'
assert solution.removeDigit('1323413', '3') == '132413'
