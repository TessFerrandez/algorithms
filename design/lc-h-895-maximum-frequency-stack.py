from collections import Counter, defaultdict


class FreqStack:
    def __init__(self):
        self.frequencies = Counter()
        self.group = defaultdict(list)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        frequency = self.frequencies[val] + 1
        self.frequencies[val] = frequency
        if frequency > self.max_frequency:
            self.max_frequency = frequency
        self.group[frequency].append(val)

    def pop(self) -> int:
        val = self.group[self.max_frequency].pop()
        self.frequencies[val] -= 1
        if not self.group[self.max_frequency]:
            self.max_frequency -= 1
        return val


freq_stack = FreqStack()
freq_stack.push(5)  # The stack is [5]
freq_stack.push(7)  # The stack is [5,7]
freq_stack.push(5)  # The stack is [5,7,5]
freq_stack.push(7)  # The stack is [5,7,5,7]
freq_stack.push(4)  # The stack is [5,7,5,7,4]
freq_stack.push(5)  # The stack is [5,7,5,7,4,5]
assert freq_stack.pop() == 5    # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
assert freq_stack.pop() == 7    # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
assert freq_stack.pop() == 5    # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
assert freq_stack.pop() == 4    # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
