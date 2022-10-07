class LUPrefix:
    def __init__(self, n: int):
        self.content = [False] * n
        self.prefix = 0
        self.n = n

    def upload(self, video: int) -> None:
        self.content[video - 1] = True

        while self.prefix < self.n and self.content[self.prefix]:
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix


server = LUPrefix(4)
server.upload(3)
assert server.longest() == 0
server.upload(1)
assert server.longest() == 1
server.upload(2)
assert server.longest() == 3
server.upload(4)
assert server.longest() == 4
