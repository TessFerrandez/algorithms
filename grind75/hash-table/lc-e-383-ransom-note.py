from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for ch in ransom:
            if mag[ch] < ransom[ch]:
                return False
        return True


solution = Solution()
assert not solution.canConstruct('a', 'b')
assert not solution.canConstruct('aa', 'ab')
assert solution.canConstruct('aa', 'aab')
