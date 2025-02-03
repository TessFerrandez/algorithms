# array, hash table, math, design, randomized
import random


class RandomizedSet:
    def __init__(self):
        self.random_set = set()

    def insert(self, val: int) -> bool:
        if val in self.random_set:
            return False
        self.random_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            self.random_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        n = len(self.random_set)
        index = random.randint(0, n - 1)
        return list(self.random_set)[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
randomized_set = RandomizedSet()
assert(randomized_set.insert(1))
assert(not randomized_set.remove(2))
assert(randomized_set.insert(2))
assert(randomized_set.getRandom() in [1, 2])
assert(randomized_set.remove(1))
assert(not randomized_set.insert(2))
assert(randomized_set.getRandom() == 2)
