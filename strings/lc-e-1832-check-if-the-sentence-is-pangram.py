class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = {ch for ch in sentence}
        return len(letters) == 26


solution = Solution()
assert solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
assert not solution.checkIfPangram("leetcode")
