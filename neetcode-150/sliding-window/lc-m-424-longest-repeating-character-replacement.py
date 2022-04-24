from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = max_length = 0

        # keeps track of the counts of chars in the
        # current sub-sequence
        count = defaultdict(int)

        for i in range(len(s)):
            # found a new character
            count[s[i]] += 1

            # max number of same char
            max_count = max(max_count, count[s[i]])

            # maximum length with current char is max count + k
            if max_length < k + max_count:
                max_length += 1
            else:
                # correct by removing the first character
                count[s[i - max_length]] -= 1

        return max_length


solution = Solution()
assert solution.characterReplacement('ABAB', 2) == 4
assert solution.characterReplacement('AABABBA', 1) == 4
