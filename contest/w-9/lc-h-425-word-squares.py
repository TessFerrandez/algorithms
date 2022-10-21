from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.words = []

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ''' try a word, add next row, and backtrack if you can't find it '''

        def insert(word):
            current = root

            for ch in word:
                if ch not in current.children:
                    current.children[ch] = TrieNode()
                current = current.children[ch]
                current.words.append(word)

        def get_words(prefix):
            current = root

            for ch in prefix:
                if ch not in current.children:
                    return []
                current = current.children[ch]

            return current.words

        def backtrack(index, current_words):
            if index == word_len:
                answer.append(current_words[:])     # we found a solution
                return

            prefix = ''.join(word[index] for word in current_words)
            prefix_words = get_words(prefix)

            for word in prefix_words:
                current_words.append(word)
                backtrack(index + 1, current_words)
                current_words.pop()

        root = TrieNode()

        # build trie
        for word in words:
            insert(word)

        # backtracking
        answer = []
        word_len = len(words[0])

        for word in words:
            backtrack(1, [word])

        return answer


solution = Solution()
assert solution.wordSquares(["area","lead","wall","lady","ball"]) == [["wall", "area", "lead", "lady"], ["ball", "area", "lead", "lady"]]
assert solution.wordSquares(["abat","baba","atan","atal"]) == [["baba","abat","baba","atan"],["baba", "abat", "baba", "atal"]]
