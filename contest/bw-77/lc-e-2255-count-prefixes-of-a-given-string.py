from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(1 for word in words if s.startswith(word))


solution = Solution()
assert solution.countPrefixes(["a","b","c","ab","bc","abc"], "abc") == 3
assert solution.countPrefixes(["a","a"], "aa") == 2
assert solution.countPrefixes(["b"], "aa") == 0
