class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in 'aeiouAEIOU':
                left += 1
            elif s[right] not in 'aeiouAEIOU':
                right -= 1
            else:
                s[right], s[left] = s[left], s[right]
                left += 1
                right -= 1

        return ''.join(s)


solution = Solution()
assert solution.reverseVowels("hello") == "holle"
assert solution.reverseVowels("leetcode") == "leotcede"
assert solution.reverseVowels("aA") == "Aa"
