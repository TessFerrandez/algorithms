from bisect import bisect_left
from typing import List

from numpy import char


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.words = []

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.words.append(word)
            node.words.sort()
            while len(node.words) > 3:
                node.words.pop()

    def search(self, word):
        result = []
        node = self.root
        for ch in word:
            if ch not in node.children:
                break
            node = node.children[ch]
            result.append(node.words[:])
        l_remain = len(word) - len(result)
        for _ in range(l_remain):
            result.append([])
        return result


class Solution:
    # binary search
    def suggestedProducts1(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix, result = '', []

        i = 0
        for ch in searchWord:
            prefix += ch
            i = bisect_left(products, prefix, i)
            result.append([word for word in products[i: i + 3] if word.startswith(prefix)])

        return result

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        return trie.search(searchWord)


solution = Solution()
print(solution.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
print(solution.suggestedProducts(["havana"], "havana"))
print(solution.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags"))


