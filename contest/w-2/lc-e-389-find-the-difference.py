from typing import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count1 = Counter(s)
        count2 = Counter(t)

        for ch in count2:
            if ch not in count1 or count1[ch] < count2[ch]:
                return ch


solution = Solution()
assert solution.findTheDifference("abcd", "abcde") == "e"
assert solution.findTheDifference("", "y") == "y"
