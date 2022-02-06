class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = ['0'] * size
        self.flip_bits = ['1'] * size
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.bits[idx] == '0':
            self.ones += 1
        self.bits[idx] = '1'
        self.flip_bits[idx] = '0'

    def unfix(self, idx: int) -> None:
        if self.bits[idx] == '1':
            self.ones -= 1
        self.bits[idx] = '0'
        self.flip_bits[idx] = '1'

    def flip(self) -> None:
        self.bits, self.flip_bits = self.flip_bits, self.bits
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return ''.join(self.bits)


def test1():
    bs = Bitset(5)
    assert bs.toString() == '00000'
    bs.fix(3)
    assert bs.toString() == '00010'
    bs.fix(1)
    assert bs.toString() == '01010'
    bs.flip()
    assert bs.toString() == '10101'
    assert not bs.all()
    bs.unfix(0)
    assert bs.toString() == '00101'
    bs.flip()
    assert bs.toString() == '11010'
    assert bs.one()
    bs.unfix(0)
    assert bs.toString() == '01010'
    assert bs.count() == 2
    assert bs.toString() == '01010'


test1()
