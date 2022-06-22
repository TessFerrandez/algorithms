from collections import defaultdict


class Trie:
    def __init__(self):
        self.links = defaultdict(self.__class__)
        self.index = None
        # holds indices which contain this prefix and whose remainder is a palindrome
        self.pali_indices = set()

    def insert(self, word, i):
        trie = self
        for j, ch in enumerate(word):
            trie = trie.links[ch]
            if word[j + 1:] and is_palindrome(word[j + 1:]):
                trie.pali_indices.add(i)
        trie.index = i


def is_palindrome(word):
    i, j = 0, len(word) - 1
    while i <= j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def palindromePairs(self, words):
        '''Find pairs of palindromes in O(n*k^2) time and O(n*k) space.'''
        root = Trie()
        res = []
        for i, word in enumerate(words):
            if not word:
                continue
            root.insert(word[::-1], i)
        for i, word in enumerate(words):
            if not word:
                continue
            trie = root
            for j, ch in enumerate(word):
                if ch not in trie.links:
                    break
                trie = trie.links[ch]
                if is_palindrome(word[j + 1:]) and trie.index is not None and trie.index != i:
                    # if this word completes to a palindrome and the prefix is a word, complete it
                    res.append([i, trie.index])
            else:
                # this word is a reverse suffix of other words, combine with those that complete to a palindrome
                for pali_index in trie.pali_indices:
                    if i != pali_index:
                        res.append([i, pali_index])
        if '' in words:
            j = words.index('')
            for i, word in enumerate(words):
                if i != j and is_palindrome(word):
                    res.append([i, j])
                    res.append([j, i])
        return res


solution = Solution()

assert solution.palindromePairs(["abcd","dcba","lls","s","sssll"]) == [[0, 1], [1, 0], [2, 4], [3, 2]]
assert solution.palindromePairs(["bat","tab","cat"]) == [[0,1],[1,0]]
assert solution.palindromePairs(["a",""]) == [[0,1],[1,0]]
