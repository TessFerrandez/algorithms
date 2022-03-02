'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
'''
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        result = ''
        for ch, num in counts.most_common():
            result += ch * num
        return result


solution = Solution()
assert solution.frequencySort('tree') == 'eetr'
assert solution.frequencySort('cccaaa') == 'cccaaa'
assert solution.frequencySort('Aabb') == 'bbAa'
