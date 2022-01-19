'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lookup = {}
        words = s.split(' ')

        if len(words) != len(pattern):
            return False

        word_i = 0
        for ch in pattern:
            if ch in lookup:
                if lookup[ch] != words[word_i]:
                    return False
            else:
                if words[word_i] in lookup.values():
                    return False
                lookup[ch] = words[word_i]

            word_i += 1

        return True


solution = Solution()
assert solution.wordPattern("abba", "dog cat cat dog") == True
assert solution.wordPattern("abba", "dog cat cat fish") == False
assert solution.wordPattern("aaaa", "dog cat cat dog") == False
assert solution.wordPattern("abba", "dog dog dog dog") == False
