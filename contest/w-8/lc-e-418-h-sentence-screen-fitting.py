from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        all_words = ' '.join(sentence) + ' '
        sentence_len = len(all_words)

        current_pos = 0

        for _ in range(rows):
            current_pos += cols
            if all_words[current_pos % sentence_len] == ' ':
                current_pos += 1
            else:
                while current_pos > 0 and all_words[(current_pos - 1) % sentence_len] != ' ':
                    current_pos -= 1

        return current_pos // sentence_len


solution = Solution()
assert solution.wordsTyping(["hello", "world"], 2, 8) == 1
assert solution.wordsTyping(["a", "bcd", "e"], 3, 6) == 2
assert solution.wordsTyping(["I", "had", "apple", "pie"], 4, 5) == 1
