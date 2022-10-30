from collections import defaultdict
from typing import List


class Solution:
    # my contest solution
    def oddString1(self, words: List[str]) -> str:
        diffs = defaultdict(list)

        for word in words:
            diff = []
            prev = word[0]
            for ch in word:
                diff.append(ord(ch) - ord(prev))

            diffs[tuple(diff)].append(word)

        for diff in diffs:
            if len(diffs[diff]) == 1:
                return diffs[diff][0]

    # slightly cleaner
    def oddString(self, words: List[str]) -> str:
        diffs = defaultdict(list)

        for word in words:
            diff = [ord(ch1) - ord(ch2) for ch1, ch2 in zip(word[:-1], word[1:])]
            diffs[tuple(diff)].append(word)

        for _, words in diffs.items():
            if len(words) == 1:
                return words[0]


solution = Solution()
assert solution.oddString(["adc","wzy","abc"]) == 'abc'
assert solution.oddString(["aaa","bob","ccc","ddd"]) == 'bob'
