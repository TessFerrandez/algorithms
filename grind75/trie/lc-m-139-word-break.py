from functools import cache
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        @cache
        def is_ok(sub_string):
            if not sub_string:
                return True

            start_words = []
            current = trie.root
            current_word = ''
            for ch in sub_string:
                if ch in current.children:
                    current_word += ch
                    current = current.children[ch]
                    if current.is_end:
                        start_words.append(current_word)
                else:
                    break

            for word in start_words:
                rest = sub_string[len(word):]
                if is_ok(rest):
                    return True

            return False

        return is_ok(s)


solution = Solution()
assert solution.wordBreak("leetcode", ["leet", "code"])
assert solution.wordBreak("applepenapple", ["apple", "pen"])
assert not solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
