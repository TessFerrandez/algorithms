from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        n = len(digits)

        def letter_combos(i):
            if i == n:
                return []

            rest_combos = letter_combos(i + 1)
            if not rest_combos:
                return list(num_map[digits[i]])

            all_combos = []
            for ch in num_map[digits[i]]:
                for combo in rest_combos:
                    all_combos.append(ch + combo)
            return all_combos

        return letter_combos(0)


solution = Solution()
assert solution.letterCombinations('4') == ['g', 'h', 'i']
assert solution.letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
assert solution.letterCombinations('') == []
