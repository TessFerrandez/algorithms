class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndpoint = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.isEndpoint = True

    def search(self, word: str) -> bool:
        current = self.root

        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.isEndpoint

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True


trie = Trie()
trie.insert('apple')
assert trie.search('apple')
assert not trie.search('app')
assert trie.startsWith('app')
trie.insert('app')
assert trie.search('app')
