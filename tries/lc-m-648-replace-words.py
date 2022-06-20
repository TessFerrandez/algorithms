from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.end_of_word = True

    def get_replacement(self, word):
        current = self.root

        replacement = ''
        for ch in word:
            if ch not in current.children:
                return word
            replacement += ch
            current = current.children[ch]
            if current.end_of_word:
                return replacement
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        result = ''
        for word in sentence.split(' '):
            result += trie.get_replacement(word) + ' '

        return result.strip()


solution = Solution()
assert solution.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"
assert solution.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs") == "a a b c"
