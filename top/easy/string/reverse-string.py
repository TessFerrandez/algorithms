from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        half = n // 2

        for i in range(half):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]


solution = Solution()

string = ["h","e","l","l","o"]
solution.reverseString(string)
assert string == ["o","l","l","e","h"]

string = ["H","a","n","n","a","h"]
solution.reverseString(string)
assert string == ["h","a","n","n","a","H"]
