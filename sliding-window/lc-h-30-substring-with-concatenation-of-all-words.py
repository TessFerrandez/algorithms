from collections import Counter
from typing import List


class Solution:
    def findSubstring1(self, s: str, words: List[str]) -> List[int]:
        n, k, word_len = len(s), len(words), len(words[0])
        sub_len = k * word_len

        word_count = Counter(words)

        # checks if the sub string starting at index idx is valid
        def check(idx):
            remaining = dict(word_count)

            for i in range(idx, idx + sub_len, word_len):
                word_to_check = s[i: i + word_len]
                if word_to_check not in remaining or remaining[word_to_check] == 0:
                    return False
                remaining[word_to_check] -= 1

            return True

        results = []
        for i in range(n - sub_len + 1):
            if check(i):
                results.append(i)

        return results

    # treat the words as letters in an anagram
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, k, word_len = len(s), len(words), len(words[0])
        sub_len = k * word_len

        word_count = Counter(words)
        to_find = len(word_count)

        # do a pass word_len times
        # 0 - 3 - 6 -...
        # 1 - 4 - 7 -...
        # 2 - 5 - 8 -...

        results = []
        for offset in range(word_len):
            remaining = dict(word_count)

            # initialize first substring
            found = 0

            for i in range(k):
                current_word = s[i * word_len + offset: (i + 1) * word_len + offset]
                if current_word in remaining:
                    remaining[current_word] -= 1
                    if remaining[current_word] == 0:
                        found += 1
                    elif remaining[current_word] == -1:
                        found -= 1
            if found == to_find:
                results.append(offset)

            # go to the rest and remove/add words
            for i in range(word_len + offset, n - sub_len + 1, word_len):
                to_remove = s[i - word_len: i]
                if to_remove in remaining:
                    remaining[to_remove] += 1
                    if remaining[to_remove] == 0:
                        found += 1
                    elif remaining[to_remove] == 1:
                        found -= 1

                to_add = s[i + (word_len * (k - 1)): i + (word_len * k)]
                if to_add in remaining:
                    remaining[to_add] -= 1
                    if remaining[to_add] == 0:
                        found += 1
                    elif remaining[to_add] == -1:
                        found -= 1
                if found == to_find:
                    results.append(i)

        return results


solution = Solution()
assert solution.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]) == [13]
assert solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]) == [8]
assert solution.findSubstring("barfoothefoobarman", ["foo","bar"]) == [0, 9]
assert solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == []
assert solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) == [6, 9, 12]
