'''
MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
'''
class MyHashMap:
    def __init__(self):
        self.maps = [None] * 1001

    def put(self, key: int, value: int) -> None:
        i = key // 1000
        j = key % 1000
        if not self.maps[i]:
            self.maps[i] = [None] * 1001
        self.maps[i][j] = value

    def get(self, key: int) -> int:
        i = key // 1000
        j = key % 1000
        if not self.maps[i]:
            return -1
        return -1 if self.maps[i][j] is None else self.maps[i][j]

    def remove(self, key: int) -> None:
        i = key // 1000
        j = key % 1000
        if self.maps[i]:
            self.maps[i][j] = None


hm = MyHashMap()
hm.remove(2)
hm.put(3, 11)
hm.put(4, 13)
hm.put(15, 6)
hm.put(6, 15)
hm.put(8, 8)
hm.put(11, 0)
assert hm.get(11) == 0
hm.put(1, 10)
hm.put(12, 14)
