'''
union find for finding if sets are connected

complexity:

Time - ctor         O(n)
Time - Find         O(1)
Time - Union        O(n)
Time - Connected    O(1)
Space   O(n)
'''
class UnionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)

assert uf.connected(1, 5)
assert uf.connected(5, 7)
assert not uf.connected(4, 9)

uf.union(4, 9)
assert uf.connected(4, 9)
