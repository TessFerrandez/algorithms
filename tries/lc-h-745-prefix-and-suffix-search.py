from collections import defaultdict
from typing import List


Trie = lambda: defaultdict(Trie)
WEIGHT = False


# trie with set intersection (TLE)
class WordFilter1:
    def __init__(self, words: List[str]):
        self.trie1 = Trie()     # prefix
        self.trie2 = Trie()     # suffix
        for weight, word in enumerate(words):
            current = self.trie1
            self.add_weight(current, weight)
            for letter in word:
                current = current[letter]
                self.add_weight(current, weight)

            current = self.trie2
            self.add_weight(current, weight)
            for letter in word[:: -1]:
                current = current[letter]
                self.add_weight(current, weight)

    def add_weight(self, node, weight):
        if WEIGHT not in node:
            node[WEIGHT] = {weight}
        else:
            node[WEIGHT].add(weight)

    def f(self, prefix: str, suffix: str) -> int:
        current1 = self.trie1
        for letter in prefix:
            if letter not in current1:
                return -1
            current1 = current1[letter]

        current2 = self.trie2
        for letter in suffix[:: -1]:
            if letter not in current2:
                return -1
            current2 = current2[letter]

        return max(current1[WEIGHT] & current2[WEIGHT])


# paired trie (gives error)
class WordFilter2:
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            cur = self.trie
            cur[WEIGHT] = weight
            for i, x in enumerate(word):
                # Put all prefixes and suffixes
                tmp = cur
                for letter in word[i:]:
                    tmp = tmp[letter, None]
                    tmp[WEIGHT] = weight

                tmp = cur
                for letter in word[:-i or None][::-1]:
                    tmp = tmp[None, letter]
                    tmp[WEIGHT] = weight

                # Advance letters
                cur = cur[x, word[~i]]
                cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for a, b in map(None, prefix, suffix[::-1]):
            if (a, b) not in cur:
                return -1
            cur = cur[a, b]
        return cur[WEIGHT]


# warped words - suffix#prefix
class WordFilter(object):
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]


wf = WordFilter(['apple'])
assert wf.f('a', 'e') == 0
