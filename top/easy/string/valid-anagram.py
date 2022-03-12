from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cs, ct = Counter(s), Counter(t)

        for ch in cs:
            if ch not in ct or ct[ch] != cs[ch]:
                return False

        return True


solution = Solution()
assert solution.isAnagram('anagram', 'nagaram')
assert not solution.isAnagram('rat', 'car')
