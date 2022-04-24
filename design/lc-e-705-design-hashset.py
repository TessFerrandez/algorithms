class MyHashSet2:
    def __init__(self):
        self.hashmap = [0] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.hashmap[key] = 1

    def remove(self, key: int) -> None:
        self.hashmap[key] = 0

    def contains(self, key: int) -> bool:
        return self.hashmap[key] == 1


# multiplicative hash
class MyHashSet:
    def __init__(self):
        self.hashmap = [[] for _ in range(1 << 15)]

    def eval_hash(self, key):
        return ((key * 1031237) & (1 << 20) - 1) >> 5

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.hashmap[t]:
            self.hashmap[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.hashmap[t]:
            self.hashmap[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.hashmap[t]


hs = MyHashSet()
hs.add(1)
hs.add(2)
assert hs.contains(1)
assert not hs.contains(3)
hs.add(2)
assert hs.contains(2)
hs.remove(2)
assert not hs.contains(2)
