from random import choice, randint


class RandomizedSet1:
    def __init__(self):
        self.data = set()
        self.count = 0

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data.add(val)
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.remove(val)
            self.count -= 1
            return True
        return False

    def getRandom(self) -> int:
        idx = randint(0, self.count - 1)
        return list(self.data)[idx]


class RandomizedSet:
    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]
        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        self.data.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.data)


rset = RandomizedSet()
assert rset.insert(1)
assert not rset.remove(2)
assert rset.insert(2)
print(rset.getRandom())
assert rset.remove(1)
assert not rset.insert(2)
assert rset.getRandom() == 2
