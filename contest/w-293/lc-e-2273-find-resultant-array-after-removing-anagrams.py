from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) <= 1:
            return words

        left, right = 0, 1

        result = [words[0]]
        while right < len(words):
            if sorted(words[left]) != sorted(words[right]):
                result.append(words[right])
                left = right
                right = left + 1
            else:
                right += 1
        return result


solution = Solution()
assert solution.removeAnagrams(["a","b","c","d","e"]) == ["a","b","c","d","e"]
assert solution.removeAnagrams(["abba","baba","bbaa","cd","cd"]) == ["abba","cd"]
