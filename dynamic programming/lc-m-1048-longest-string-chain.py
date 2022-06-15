from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lens = defaultdict(list)
        chain = defaultdict(int)

        for word in words:
            lens[len(word)].append(word)

        for word_len in range(max(lens) + 1):
            for word in lens[word_len]:
                for i in range(word_len):
                    chain[word] = max(chain[word], 1 + chain[word[:i] + word[i + 1:]])

        return max(chain.values())


solution = Solution()
assert solution.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]) == 5
assert solution.longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4
assert solution.longestStrChain(["abcd","dbqca"]) == 1
