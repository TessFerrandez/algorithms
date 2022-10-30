from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        combos = [set()]

        def word_has_duplicates(word):
            return len(set(word)) < len(word)

        def words_have_duplicates(letter_set1, letter_set2):
            return letter_set1 & letter_set2 != set()

        for word in arr:
            if word_has_duplicates(word):
                continue

            word_letters = set(word)
            for combo_letters in combos:
                if not words_have_duplicates(word_letters, combo_letters):
                    combos.append(word_letters | combo_letters)

        return max(len(combo) for combo in combos)


solution = Solution()
assert solution.maxLength(['un', 'iq', 'ue']) == 4
assert solution.maxLength(['cha', 'r', 'act', 'ers']) == 6
assert solution.maxLength(['abcdefghijklmnopqrstuvwxyz']) == 26
