'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        note = Counter(ransomNote)

        for ch in note:
            if ch not in mag or mag[ch] < note[ch]:
                return False
        return True


solution = Solution()
assert not solution.canConstruct('a', 'b')
assert not solution.canConstruct('aa', 'ab')
assert solution.canConstruct('aa', 'aab')
