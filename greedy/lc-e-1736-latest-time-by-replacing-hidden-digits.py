'''
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.
'''

class Solution:
    def maximumTime(self, time: str) -> str:
        result = ''
        for i, ch in enumerate(time):
            if ch != '?':
                result += ch
            elif i == 0 and ('0' <= time[1] <= '3' or time[1] == '?'):
                result += '2'
            elif i == 0:
                result += '1'
            elif i == 1 and result[-1] == '2':
                result += '3'
            elif i == 3:
                result += '5'
            else:
                result += '9'

        return result


solution = Solution()
assert solution.maximumTime('?0:15') == '20:15'
assert solution.maximumTime('?4:03') == '14:03'
assert solution.maximumTime('2?:?0') == '23:50'
assert solution.maximumTime('0?:3?') == '09:39'
assert solution.maximumTime('1?:22') == '19:22'
