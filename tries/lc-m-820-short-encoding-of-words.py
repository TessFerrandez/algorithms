from collections import defaultdict
from functools import reduce
from typing import List


class Solution:
    # store prefixes
    def minimumLengthEncoding1(self, words: List[str]) -> int:
        good = set(words)

        for word in words:
            for k in range(1, len(word)):
                if word[k:] in good:
                    good.remove(word[k:])

        answer = 0
        for word in good:
            answer += len(word) + 1

        return answer

    # trie
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))    # remove duplicates

        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]

        # add word to answer if its node has no neighbors
        return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)


solution = Solution()
assert solution.minimumLengthEncoding(["time", "me", "bell"]) == 10     # time#bell# (0, 2, 5)
assert solution.minimumLengthEncoding(["t"]) == 2                       # t# (0)
