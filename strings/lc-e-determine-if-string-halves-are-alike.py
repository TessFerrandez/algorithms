'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
'''
def num_vowels(s):
    return sum(1 for ch in s if ch in 'aeiouAEIOU')


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        slen = len(s)
        s1 = s[:slen // 2]
        s2 = s[slen // 2:]
        return num_vowels(s1) == num_vowels(s2)


solution = Solution()
assert solution.halvesAreAlike('book') == True
assert solution.halvesAreAlike('textbook') == False
