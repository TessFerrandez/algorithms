class Bitset:
    def __init__(self, size: int):
        self.bits = [0] * size
        self.fbits = [1] * size
        self.bit_count = 0
        self.size = size

    def fix(self, idx: int) -> None:
        if self.bits[idx] == 0:
            self.bit_count += 1
        self.bits[idx] = 1
        self.fbits[idx] = 0

    def unfix(self, idx: int) -> None:
        if self.bits[idx] == 1:
            self.bit_count -= 1
        self.bits[idx] = 0
        self.fbits[idx] = 1

    def flip(self) -> None:
        self.bits, self.fbits = self.fbits, self.bits
        self.bit_count = self.size - self.bit_count

    def all(self) -> bool:
        return self.bit_count == self.size

    def one(self) -> bool:
        return self.bit_count > 0

    def count(self) -> int:
        return self.bit_count

    def toString(self) -> str:
        return ''.join(str(i) for i in self.bits)


bitset = Bitset(5)
bitset.fix(3)
bitset.fix(1)
bitset.flip()
assert not bitset.all()
bitset.unfix(0)
bitset.flip()
assert bitset.one()
bitset.unfix(0)
assert bitset.count() == 2
assert bitset.toString() == '01010'
