# string trie
from typing import List

class Solution:
    def get_prefix(self, trie):
        if len(trie) > 1:
            return ''
        if '_end' in trie:
            return ''
        first_char, next_chars = next(iter(trie.items()))
        return first_char + self.get_prefix(next_chars)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = self.make_trie(strs)
        return self.get_prefix(trie)

    def make_trie(self, words):
        END = '_end'
        root = dict()
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[END] = ''
        return root


solution = Solution()
assert solution.longestCommonPrefix([""]) == ''
assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ''