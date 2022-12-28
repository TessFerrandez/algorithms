from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        counts_1 = Counter(word1)
        counts_2 = Counter(word2)

        return sorted(counts_1.values()) == sorted(counts_2.values()) and (sorted(counts_1.keys()) == sorted(counts_2.keys()))


solution = Solution()
assert solution.closeStrings('abc', 'bca')
assert not solution.closeStrings('a', 'aa')
assert solution.closeStrings('cabbba', 'abbccc')
assert not solution.closeStrings('uau', 'ssx')
