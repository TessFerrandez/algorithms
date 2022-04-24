from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups[''.join(sorted(s))].append(s)

        return list(groups.values())


solution = Solution()
assert solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
assert solution.groupAnagrams(['']) == [['']]
assert solution.groupAnagrams(['a']) == [['a']]
