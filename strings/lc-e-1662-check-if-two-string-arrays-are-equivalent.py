from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


solution = Solution()
assert solution.arrayStringsAreEqual(['ab', 'c'], ['a', 'bc'])
assert not solution.arrayStringsAreEqual(['a', 'cb'], ['ab', 'c'])
assert solution.arrayStringsAreEqual(['abc', 'd', 'defg'], ['abcddefg'])
