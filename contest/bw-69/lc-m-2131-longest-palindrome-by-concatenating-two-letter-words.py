from collections import defaultdict
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        has_double = False

        singles = defaultdict(int)
        doubles = 0

        for word in words:
            if singles[word[::-1]] > 0:
                doubles += 1
                singles[word[::-1]] -= 1
            else:
                singles[word] += 1

        for word in singles:
            if singles[word] > 0 and word[0] == word[1]:
                has_double = True
                break

        result = doubles * 4 + (2 if has_double else 0)
        return result


solution = Solution()
assert solution.longestPalindrome(["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"]) == 14
assert solution.longestPalindrome(["lc","cl","gg"]) == 6
assert solution.longestPalindrome(["ab","ty","yt","lc","cl","ab"]) == 8
assert solution.longestPalindrome(["cc","ll","xx"]) == 2
assert solution.longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]) == 22
