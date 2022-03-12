from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for i, word in enumerate(strs):
            anagrams[''.join(sorted(word))].append(i)

        groups = []
        for anagram in anagrams:
            groups.append([strs[i] for i in anagrams[anagram]])

        return groups


solution = Solution()
assert solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
assert solution.groupAnagrams([""]) == [[""]]
assert solution.groupAnagrams(['a']) == [['a']]
