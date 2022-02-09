'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''
from collections import defaultdict
from functools import cache
from hashlib import shake_128


class Solution:
    # this super complicated solution doesn't work for teacher and butcher
    def minDistance1(self, word1: str, word2: str) -> int:
        def longest_common_subsequences(word1, word2):
            dp = defaultdict(lambda: (0, set([''])))
            for i in range(len(word1)):
                for j in range(len(word2)):
                    if word1[i] == word2[j]:
                        dp[(i, j)] = (dp[(i - 1, j - 1)][0] + 1, set(s + word1[i] for s in dp[(i - 1, j - 1)][1]))
                    else:
                        if dp[(i - 1, j)][0] == dp[(i, j - 1)][0]:
                            dp[(i, j)] = (dp[(i - 1, j)][0], dp[(i - 1, j)][1].union(dp[(i, j - 1)][1]))
                        elif dp[(i - 1, j)][0] > dp[(i, j - 1)][0]:
                            dp[(i, j)] = dp[(i - 1, j)]
                        else:
                            dp[(i, j)] = dp[(i, j - 1)]

            max_len = max(elem[0] for elem in dp.values())
            sequences = set()
            for elem in dp.values():
                if elem[0] == max_len:
                    for sequence in elem[1]:
                        sequences.add(sequence)
            return list(sequences)

        def get_letter_positions(word, sub_sequence):
            positions = defaultdict(list)
            letters = set(list(sub_sequence))
            for i, ch in enumerate(word):
                if ch in letters:
                    positions[ch].append(i)
            return positions

        def find_all_sequences(prev, sequence, positions):
            sequences = []

            for pos in positions[sequence[0]]:
                if pos > prev:
                    if len(sequence) == 1:
                        sequences.append([pos])
                    else:
                        possible = find_all_sequences(pos, sequence[1:], positions)
                        for poss in possible:
                            sequences.append([pos] + poss)

            return sequences

        def changes_needed(sequence1, sequence2, w1_len, w2_len):
            w1_prev, w2_prev = -1, -1
            s_len = len(sequence1)

            changes = 0

            for s in range(s_len):
                changes += max(sequence1[s] - w1_prev - 1, sequence2[s] - w2_prev - 1)
                w1_prev, w2_prev = sequence1[s], sequence2[s]

            changes += max(w1_len - w1_prev - 1, w2_len - w2_prev - 1)
            return changes

        w1_len = len(word1)
        w2_len = len(word2)

        if w1_len == 0:
            return w2_len

        if w2_len == 0:
            return w1_len

        sub_sequences = longest_common_subsequences(word1, word2)
        min_changes = 10 ** 9

        for sub_sequence in sub_sequences:
            # print(sub_sequence)
            if len(sub_sequence) == 0:
                return max(w1_len, w2_len)

            word1_pos = get_letter_positions(word1, sub_sequence)
            word2_pos = get_letter_positions(word2, sub_sequence)

            w1_sequences = find_all_sequences(-1, sub_sequence, word1_pos)
            w2_sequences = find_all_sequences(-1, sub_sequence, word2_pos)

            for seq1 in w1_sequences:
                for seq2 in w2_sequences:
                    min_changes = min(min_changes, changes_needed(seq1, seq2, w1_len, w2_len))

        # print(min_changes)
        return min_changes

    # recursive: TLE
    def minDistance_rec(self, word1: str, word2: str) -> int:
        def match(s1, s2, i, j):
            if len(s1) == i:
                return len(s2) - j

            if len(s2) == j:
                return len(s1) - i

            if s1[i] == s2[j]:
                return match(s1, s2, i + 1, j + 1)
            else:
                insert = match(s1, s2, i, j + 1)
                delete = match(s1, s2, i + 1, j)
                replace = match(s1, s2, i + 1, j + 1)
                return min(insert, delete, replace) + 1

        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        return match(word1, word2, 0, 0)

    # memo version
    def minDistance_mem(self, word1: str, word2: str) -> int:
        def match(s1, s2, i, j, cache):
            if len(s1) == i:
                return len(s2) - j

            if len(s2) == j:
                return len(s1) - i

            if cache[i][j] != -1:
                return cache[i][j]

            if s1[i] == s2[j]:
                cache[i][j] = match(s1, s2, i + 1, j + 1, cache)
            else:
                insert = match(s1, s2, i, j + 1, cache)
                delete = match(s1, s2, i + 1, j, cache)
                replace = match(s1, s2, i + 1, j + 1, cache)
                cache[i][j] = min(insert, delete, replace) + 1

            return cache[i][j]

    # dp version
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        matched = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            matched[i][0] = i

        for j in range(len(word2) + 1):
            matched[0][j] = j

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    matched[i + 1][j + 1] = matched[i][j]
                else:
                    matched[i + 1][j + 1] = min(matched[i][j + 1], matched[i + 1][j], matched[i][j]) + 1

        return matched[len(word1)][len(word2)]


solution = Solution()
assert solution.minDistance('a', 'ab') == 1
assert solution.minDistance('teacher', 'botcher') == 3
assert solution.minDistance('horse', 'ros') == 3
assert solution.minDistance('intention', 'execution') == 5
assert solution.minDistance('intentions', 'executiond') == 6
