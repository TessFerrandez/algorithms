class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


solution = Solution()
assert solution.isAnagram("anagram", "nagaram")
assert not solution.isAnagram("rat", "car")
