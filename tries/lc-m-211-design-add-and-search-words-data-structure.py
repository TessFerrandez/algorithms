class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(start, root):
            current = root

            for i in range(start, len(word)):
                ch = word[i]

                if ch == '.':
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if ch not in current.children:
                        return False
                    current = current.children[ch]
            return current.end_of_word

        return dfs(0, self.root)


dictionary = WordDictionary()
dictionary.addWord('bad')
dictionary.addWord('dad')
dictionary.addWord('mad')
assert not dictionary.search('pad')
assert dictionary.search('bad')
assert dictionary.search('.ad')
assert dictionary.search('b..')
