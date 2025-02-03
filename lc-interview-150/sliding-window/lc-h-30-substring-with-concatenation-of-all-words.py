from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        string_length = len(s)
        num_words = len(words)
        word_len = len(words[0])
        substr_len = num_words * word_len

        word_counts = Counter(words)
        words_to_find = len(word_counts)

        substr_starts = []

        # do a pass word_len times to cover all possible starting points
        # ex for word_len = 3, pass 036..., 147..., 258...
        for start in range(word_len):
            remaining_words = dict(word_counts)

            # initialize the sliding window with the first substring
            words_found = 0
            for i in range(num_words):
                current_word = s[start + i * word_len: start + (i + 1) * word_len]
                if current_word in remaining_words:
                    remaining_words[current_word] -= 1
                    if remaining_words[current_word] == 0:
                        words_found += 1
                    elif remaining_words[current_word] == -1:
                        words_found -= 1
                if words_found == words_to_find:
                    substr_starts.append(start)

            # slide the window one step forward at a time
            for i in range(word_len + start, string_length - substr_len + 1, word_len):
                # remove the word we lost (from the left)
                lost_word = s[i - word_len: i]
                if lost_word in remaining_words:
                    remaining_words[lost_word] += 1
                    if remaining_words[lost_word] == 0:
                        words_found += 1
                    elif remaining_words[lost_word] == 1:
                        words_found -= 1

                # add the word we gained (to the right)
                gained_word = s[i + (word_len * (num_words - 1)): i + substr_len]
                if gained_word in remaining_words:
                    remaining_words[gained_word] -= 1
                    if remaining_words[gained_word] == 0:
                        words_found += 1
                    elif remaining_words[gained_word] == -1:
                        words_found -= 1

                if words_found == words_to_find:
                    substr_starts.append(i)

        return substr_starts


solution = Solution()
assert solution.findSubstring('barfoothefoobarman', ['foo', 'bar']) == [0, 9]
assert solution.findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']) == []
assert solution.findSubstring('barfoofoobarthefoobarman', ['bar', 'foo', 'the']) == [6, 9, 12]
