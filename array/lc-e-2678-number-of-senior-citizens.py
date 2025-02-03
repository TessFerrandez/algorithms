from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for senior in details if int(senior[11:13]) > 60)


solution = Solution()
assert solution.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]) == 2
assert solution.countSeniors(["1313579440F2036","2921522980M5644"]) == 0
