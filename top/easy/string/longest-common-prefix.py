from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        if n == 1:
            return strs[0]

        longest_prefix = ''
        first_word = strs[0]
        first_n = len(first_word)

        for i in range(1, first_n + 1):
            prefix = first_word[:i]
            for word in strs[1:]:
                if not word.startswith(prefix):
                    return longest_prefix
            longest_prefix = prefix

        return longest_prefix


solution = Solution()
assert solution.longestCommonPrefix(["flower","flow","flight"]) == 'fl'
assert solution.longestCommonPrefix(["dog","racecar","car"]) == ''
assert solution.longestCommonPrefix(["fl", "flower","flow","flight"]) == 'fl'
