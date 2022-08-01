from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # count maximum occurrence of a ch in all words in words2
        all_counts2 = {}
        for word in words2:
            counts = Counter(word)
            for ch in counts:
                if ch not in all_counts2:
                    all_counts2[ch] = counts[ch]
                else:
                    all_counts2[ch] = max(all_counts2[ch], counts[ch])

        def is_match(word):
            counts = Counter(word)
            for ch in all_counts2:
                if ch not in counts or counts[ch] < all_counts2[ch]:
                    return False
            return True

        return list(filter(is_match, words1))


solution = Solution()
assert solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]) == ["facebook","google","leetcode"]
assert solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l", "e"]) == ["apple","google","leetcode"]
