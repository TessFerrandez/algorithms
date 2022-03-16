from typing import List


class Solution:
    def letterCombinations1(self, digits: str) -> List[str]:
        if not digits:
            return []

        pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        n = len(digits)
        combos = []

        def dfs(i, path):
            if i >= n:
                combos.append(path)
                return

            letters = pad[digits[i]]
            for letter in letters:
                dfs(i + 1, path + letter)

        dfs(0, '')
        return combos

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        n = len(digits)

        combos = list(pad[digits[-1]])

        for i in range(n - 2, -1, -1):
            letters = pad[digits[i]]
            new_combos = []
            for letter in letters:
                for combo in combos:
                    new_combos.append(letter + combo)
            combos = new_combos

        return combos


solution = Solution()
assert solution.letterCombinations('23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
assert solution.letterCombinations('') == []
assert solution.letterCombinations('2') == ['a', 'b', 'c']
