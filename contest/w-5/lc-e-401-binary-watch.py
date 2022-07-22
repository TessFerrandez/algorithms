from collections import defaultdict
from typing import List


class Solution:
    # my solution
    def readBinaryWatch1(self, turnedOn: int) -> List[str]:
        digits = defaultdict(list)
        for i in range(60):
            digits[bin(i).count('1')].append(i)

        possible = []
        for i in range(turnedOn + 1):
            j = turnedOn - i
            for hr in digits[i]:
                if hr <= 11:
                    time = str(hr) + ':'
                    if len(digits[j]) > 0:
                        for min in digits[j]:
                            min_time = ''
                            if min < 10:
                                min_time = '0' + str(min)
                            else:
                                min_time = str(min)
                            possible.append(time + min_time)
        return possible

    # more condensed
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return ['%d:%02d' % (h, m)
                for h in range(12)
                for m in range(60)
                if (bin(h) + bin(m)).count('1') == turnedOn]


solution = Solution()
assert solution.readBinaryWatch(1) == ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00']
assert solution.readBinaryWatch(9) == []
