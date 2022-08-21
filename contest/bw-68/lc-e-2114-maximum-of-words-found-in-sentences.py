from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0

        for sentence in sentences:
            max_words = max(max_words, len(sentence.split(' ')))

        return max_words


solution = Solution()
assert solution.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]) == 6
assert solution.mostWordsFound(["please wait", "continue to fight", "continue to win"]) == 3
