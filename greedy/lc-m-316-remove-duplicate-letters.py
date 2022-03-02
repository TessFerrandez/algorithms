'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
'''
from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = defaultdict(int)
        stack = []

        for ch in s:
            freq[ch] += 1

        for ch in s:
            if ch in stack:
                freq[ch] -= 1
                continue

            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                stack.pop()

            stack.append(ch)
            freq[ch] -= 1

        return ''.join(stack)


solution = Solution()
assert solution.removeDuplicateLetters('bcabc') == 'abc'
assert solution.removeDuplicateLetters('cbacdcbc') == 'acdb'
