from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if not digits:
            return []

        combos = letters[digits[-1]]

        for i in range(len(digits) - 2, -1, -1):
            new_letters = letters[digits[i]]
            new_combos = []
            for letter in new_letters:
                for combo in combos:
                    new_combos.append(letter + combo)
            combos = new_combos

        return combos


solution = Solution()
assert solution.letterCombinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert solution.letterCombinations('') == []
assert solution.letterCombinations('2') == ['a', 'b', 'c']
