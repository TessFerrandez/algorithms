class Solution:
    def has_vowel(self, word: str) -> bool:
        for char in word:
            if char in "aeiouAEIOU":
                return True
        return False

    def has_consonant(self, word: str) -> bool:
        for char in word:
            if char not in "aeiouAEIOU0123456789":
                return True
        return False

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        if not self.has_vowel(word):
            return False
        if not self.has_consonant(word):
            return False
        return True


solution = Solution()
assert solution.isValid("234Adas")
assert not solution.isValid("b3")
assert not solution.isValid("a3$e")
assert solution.isValid("AhI")
