from typing import List


class ATM:
    def __init__(self):
        self.count = [0, 0, 0, 0, 0]
        self.notes = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        i = 0
        for note in banknotesCount:
            self.count[i] += note
            i += 1

    def withdraw(self, amount: int) -> List[int]:
        notes_taken = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            possible = amount // self.notes[i]
            if possible > 0 and self.count[i] > 0:
                taken = min(possible, self.count[i])
                amount -= taken * self.notes[i]
                notes_taken[i] = taken

        if amount != 0:
            return [-1]
        for i, note in enumerate(notes_taken):
            self.count[i] -= note

        return notes_taken


atm = ATM()
atm.deposit([0, 0, 1, 2, 1])
assert atm.withdraw(600) == [0, 0, 1, 0, 1]
atm.deposit([0, 1, 0, 1, 1])
assert atm.withdraw(600) == [-1]
assert atm.withdraw(550) == [0, 1, 0, 0, 1]
