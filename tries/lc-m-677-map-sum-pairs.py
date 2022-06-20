from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.val = 0

    def update(self, diff):
        self.val += diff


class MapSum:
    def __init__(self):
        self.maps = defaultdict(int)
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        diff = val - self.maps[key]
        self.maps[key] = val

        current = self.root

        for ch in key:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current.children[ch].update(diff)
            current = current.children[ch]

    def sum(self, prefix: str) -> int:
        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return 0
            current = current.children[ch]

        return current.val


map_sum = MapSum()
map_sum.insert('apple', 3)
print(map_sum.sum('ap'))
map_sum.insert('app', 2)
print(map_sum.sum('ap'))
map_sum.insert('apple', 5)
print(map_sum.sum('ap'))
