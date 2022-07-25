from collections import defaultdict
from heapq import heappop, heappush
from sortedcontainers import SortedList


# TLE
class NumberContainers2:
    def __init__(self):
        self.indices = {}
        self.numbers = defaultdict(list)

    def remove(self, number, idx):
        removed = []
        while True:
            index = heappop(self.numbers[number])
            if index == idx:
                break
            else:
                removed.append(index)
        while removed:
            heappush(self.numbers[number], removed.pop())

    def change(self, index: int, number: int) -> None:
        if index in self.indices:
            num = self.indices[index]
            del self.indices[index]
            self.remove(num, index)
        self.indices[index] = number
        heappush(self.numbers[number], index)

    def find(self, number: int) -> int:
        if not self.numbers[number]:
            return -1
        index = heappop(self.numbers[number])
        heappush(self.numbers[number], index)
        return index

class NumberContainers:
    def __init__(self):
        self.numbers = defaultdict(SortedList)
        self.indices = {}

    def change(self, index: int, number: int) -> None:
        if index in self.indices:
            old = self.indices[index]
            self.numbers[old].discard(index)
            if not self.numbers[old]:
                del self.numbers[old]
        self.numbers[number].add(index)
        self.indices[index] = number

    def find(self, number: int) -> int:
        if number in self.numbers:
            return self.numbers[number][0]
        return -1


"""
nc = NumberContainers()
print(nc.find(10))
nc.change(2, 10)
nc.change(1, 10)
nc.change(3, 10)
nc.change(5, 10)
print(nc.find(10))
nc.change(1, 20)
print(nc.find(10))
"""
methods = ["change","change","change","find","change","find","find","change","find","find","find","change","find","change","change","find","find","change","find","change","change","find","find","find","change","find","find","change","find","find","find","change","find","change","change","find","change","change","change","change","find","change","change","find","change","find","find","change","change","find","change","find","change","change","find","change","change","find","change","find","change","find","find","find","change","find","find","change","change","find","change","change","find","change","change","find","find","change","find","change","change","find","find","find","find","change","find","change","find","change","change","find","change","find","change","change","change","change","find","find","find","change","change","change","change","change","find","change","change","change","find","change","change","find","change","change","find","change","change","change","change","change","change","find","find","find","find","change","find","find","find","find","change","find","change","find","find","find","find","change","find","find","change","find","find","change","change","change","change","change","change","find","find","change","change","change","change","find","change","change","change","change","change","change","change","change","find","change","find","change","find","change","change","change","change","find","change","find","change","change","change","change","change","change","change","change","change","change","find","change","change","find","change","change","change","find","find","change","find","find"]
params = [[158,9],[75,85],[75,187],[77],[109,113],[184],[77],[17,191],[113],[35],[184],[164,119],[9],[19,151],[142,50],[77],[85],[35,164],[184],[118,164],[3,164],[184],[113],[135],[72,105],[9],[187],[34,105],[135],[164],[135],[20,164],[187],[158,184],[44,50],[191],[164,50],[20,191],[158,191],[107,113],[187],[158,50],[142,9],[151],[35,119],[113],[105],[127,77],[164,164],[187],[72,191],[113],[132,164],[7,9],[85],[71,187],[7,187],[9],[20,185],[35],[7,151],[119],[135],[77],[155,187],[164],[135],[183,151],[110,164],[50],[20,85],[19,9],[85],[175,9],[116,105],[187],[164],[107,35],[185],[147,184],[109,184],[35],[184],[187],[113],[178,85],[9],[178,151],[85],[107,164],[116,135],[113],[107,164],[77],[116,35],[172,35],[200,187],[142,50],[50],[187],[105],[127,9],[34,164],[178,135],[183,50],[34,35],[184],[147,77],[172,35],[132,151],[119],[7,185],[109,185],[187],[110,135],[175,35],[35],[127,187],[71,164],[188,9],[35,50],[107,191],[158,119],[85],[50],[35],[77],[183,164],[119],[9],[77],[50],[164,9],[151],[172,77],[50],[135],[113],[77],[200,9],[77],[184],[142,105],[119],[9],[75,185],[142,113],[127,119],[110,85],[7,135],[127,185],[185],[77],[200,50],[164,164],[19,35],[172,113],[135],[178,35],[72,35],[142,85],[3,113],[109,151],[110,77],[35,119],[75,164],[105],[142,113],[164],[127,105],[119],[110,135],[158,35],[35,164],[35,9],[135],[178,50],[119],[73,185],[19,85],[155,151],[44,187],[116,191],[158,35],[110,191],[72,187],[7,9],[17,135],[35],[200,185],[142,185],[164],[175,187],[188,185],[172,50],[9],[119],[110,191],[35],[35]]
results = [None,None,None,-1,None,-1,-1,None,109,-1,-1,None,158,None,None,-1,-1,None,-1,None,None,-1,109,-1,None,158,75,None,-1,3,-1,None,75,None,None,17,None,None,None,None,75,None,None,19,None,107,34,None,None,75,None,107,None,None,-1,None,None,142,None,-1,None,35,-1,127,None,3,-1,None,None,44,None,None,20,None,None,71,3,None,-1,None,None,107,109,71,-1,None,19,None,20,None,None,-1,None,127,None,None,None,None,44,71,34,None,None,None,None,None,109,None,None,None,35,None,None,71,None,None,34,None,None,None,None,None,None,20,35,34,147,None,158,19,147,35,None,132,None,35,110,-1,147,None,147,-1,None,158,19,None,None,None,None,None,None,75,147,None,None,None,None,7,None,None,None,None,None,None,None,None,-1,None,71,None,35,None,None,None,None,7,None,-1,None,None,None,None,None,None,None,None,None,None,34,None,None,71,None,None,None,7,-1,None,34,34]

nc = NumberContainers()
for i in range(len(methods)):
    if methods[i] == "change":
        idx, number = params[i]
        nc.change(idx, number)
    else:
        number = params[i][0]
        expected_idx = results[i]
        result = nc.find(number)
        assert result == expected_idx
