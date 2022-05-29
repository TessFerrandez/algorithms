from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def encode(word):
            encoded = 0
            for ch in word:
                encoded |= 1 << ord(ch) - ord('a')
            return encoded

        max_product = 0
        encoded = []
        for word in words:
            current_len, current_code = len(word), encode(word)
            for word_len, code in encoded:
                if code & current_code == 0:
                    max_product = max(max_product, word_len * current_len)
            encoded.append((current_len, current_code))

        return max_product


solution = Solution()
assert solution.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]) == 16
assert solution.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]) == 4
assert solution.maxProduct(["a","aa","aaa","aaaa"]) == 0
