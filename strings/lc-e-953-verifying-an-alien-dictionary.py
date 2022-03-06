'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
'''
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i, ch in enumerate(order):
            order_map[ch] = i

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    # all letters up to j are the same
                    # but i + 1 is shorter
                    return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        # i + 1 is lexiographically smaller
                        return False
                    # i + 1 is lexiographically larger
                    break

        return True


solution = Solution()
assert solution.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
assert not solution.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
assert not solution.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
