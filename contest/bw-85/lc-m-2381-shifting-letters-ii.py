from typing import List


class Solution:
    # tle
    def shiftingLetters1(self, s: str, shifts: List[List[int]]) -> str:
        total_shifts = [0] * len(s)

        for start, end, dir in shifts:
            dir = -1 if dir == 0 else dir
            for i in range(start, end + 1):
                total_shifts[i] += dir

        result_str = ''
        for i, ch in enumerate(s):
            result_str += chr(ord('a') + (ord(ch) - ord('a') + total_shifts[i]) % 26)

        return result_str

    # increasing or decreasing intervals
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cum_shifts = [0] * (len(s) + 1)

        for start, end, dir in shifts:
            if dir == 0:
                cum_shifts[start] -= 1
                cum_shifts[end + 1] += 1
            else:
                cum_shifts[start] += 1
                cum_shifts[end + 1] -= 1

        cum_sum = 0
        result_str = ''
        for i, ch in enumerate(s):
            cum_sum += cum_shifts[i]
            result_str += chr(((ord(ch) + cum_sum - ord('a')) % 26) + ord('a'))

        return result_str


solution = Solution()
assert solution.shiftingLetters('abc', [[0,1,0],[1,2,1],[0,2,1]]) == 'ace'
assert solution.shiftingLetters('dztz', [[0,0,0],[1,1,1]]) == 'catz'
