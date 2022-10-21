from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)

        for row in range(rows):
            for col in range(len(words[row])):
                if col >= rows or row >= len(words[col]):
                    return False
                if words[row][col] != words[col][row]:
                    return False
        return True


solution = Solution()
assert solution.validWordSquare(["abcd","bnrt","crmy","dtye"])
assert solution.validWordSquare(["abcd","bnrt","crm","dt"])
assert not solution.validWordSquare(["ball","area","read","lady"])
