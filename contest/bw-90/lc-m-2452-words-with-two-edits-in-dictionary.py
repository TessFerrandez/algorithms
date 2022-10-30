from typing import List


class Solution:
    # my solution during competition
    def twoEditWords1(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])

        def is_match(word1, word2):
            off_count = 0
            for i in range(n):
                if word1[i] != word2[i]:
                    off_count += 1
                    if off_count > 2:
                        return False
            return True

        def has_match(word):
            for dict_word in dictionary:
                if is_match(word, dict_word):
                    return True

            return False

        result = []

        for word in queries:
            if has_match(word):
                result.append(word)

        return result

    # shorter
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []

        for word in queries:
            if any(sum(ch1 != ch2 for ch1, ch2 in zip(word, dict_word)) <= 2 for dict_word in dictionary):
                result.append(word)

        return result


solution = Solution()
assert solution.twoEditWords(["word","note","ants","wood"], ["wood","joke","moat"]) == ["word","note","wood"]
assert solution.twoEditWords(["yes"], ["not"]) == []
