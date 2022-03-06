'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        result = ''
        for i in range(n):
            result += word1[i]
            result += word2[i]
        if len(word1) > len(word2):
            result += word1[n:]
        else:
            result += word2[n:]
        return result


solution = Solution()
assert solution.mergeAlternately('abc', 'pqr') == 'apbqcr'
assert solution.mergeAlternately('ab', 'pqrs') == 'apbqrs'
assert solution.mergeAlternately('abcd', 'pq') == 'apbqcd'
