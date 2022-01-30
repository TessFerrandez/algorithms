'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''
from typing import List
from functools import lru_cache


class Solution:
    # my solution with memoization
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        lens = {word: len(word) for word in wordDict}
        wordDict = sorted(wordDict, key=len, reverse=True)

        @lru_cache()
        def is_valid(remaining):
            if remaining == "":
                return True

            for word in wordDict:
                if remaining.startswith(word):
                    if is_valid(remaining[lens[word]:]):
                        return True

            return False

        return is_valid(s)

    # from discussion - dp based on length
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i - len(word) + 1: i + 1] and (dp[i - len(word)] or i - len(word) == -1):
                    dp[i] = True
        return dp[-1]


solution = Solution()
assert solution.wordBreak("abcd", ["a", "abc", "b", "cd"])
assert not solution.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])
assert solution.wordBreak('leetcode', ['leet', 'code'])
assert solution.wordBreak('applepenapple', ['apple', 'pen'])
