class DataStream:

    def __init__(self, value: int, k: int):
        self.count = 0
        self.k = k
        self.value = value

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        return self.count >= self.k


stream = DataStream(4, 3)
assert not stream.consec(4)
assert not stream.consec(4)
assert stream.consec(4)
assert not stream.consec(3)
