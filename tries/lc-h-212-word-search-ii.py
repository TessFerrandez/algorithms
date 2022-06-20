'''
1. When constructing the Trie, for each node, count number of words that include the word
2. In DFS, if we find a word, decrease the number of words of all corresponding nodes
3. If the nodes number of words is 0, we stop searching bc all the words that include the node are in the results list
'''
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        self.parent = None
        self.num_words = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node.children[ch].parent = node     # add the parent node
            node = node.children[ch]
            node.num_words += 1                 # increase the number of words that include this node

        node.is_word = True
        node.word = word

    def find(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return None
            current = current.children[ch]
        return current

    def shadow_delete(self, word):              # shadow delete the word from the Trie
        node = self.find(word)
        if node is None:
            return

        node.is_word = False
        while node != self.root:
            node.num_words -= 1
            node = node.parent
        return


DIRECTIONS = [(0,1), (0,-1), (1, 0), (-1, 0)]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        result = []
        trie = Trie()

        def dfs(node, row, col):
            if node.is_word:
                result.append(node.word)
                trie.shadow_delete(node.word)

            if not (0 <= row < len(board) and 0 <= col < len(board[0])):    # outside the boundary
                return

            node = node.children.get(board[row][col])
            if node is None:
                return
            if node.num_words == 0:                                         # pruning: stop searching if every word that includes this node is added to the result list
                return

            tmp = board[row][col]
            board[row][col] = '#'
            for dr, dc in DIRECTIONS:
                new_row, new_col = row + dr, col + dc
                dfs(node, new_row, new_col)
            board[row][col] = tmp

        for word in words:
            trie.insert(word)

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(trie.root, r, c)

        return result


solution = Solution()
print(solution.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print(solution.findWords([["a","b"],["c","d"]], ["abcb"]))
