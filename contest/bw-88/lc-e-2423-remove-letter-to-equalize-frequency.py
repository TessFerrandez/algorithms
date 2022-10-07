from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        letter_counts = list(sorted(Counter(word).values()))

        # if we only have one (of one char) - remove it (a.k.a reduce the count to zero)
        # and see if all our letters have the same count - or if we have an empty array
        if letter_counts[0] == 1 and len(set(letter_counts[1:])) <= 1:
            return True

        # otherwise - let's see if the last one is the only "odd one out"
        # reduce the number of instances of this char
        letter_counts[-1] -= 1

        # if all the characters are now the same, we are good
        return len(set(letter_counts)) == 1


solution = Solution()
assert not solution.equalFrequency("ddaccb")
assert solution.equalFrequency("aabbccc")
assert solution.equalFrequency("abbcc")
assert solution.equalFrequency("aca")
assert solution.equalFrequency("bac")
assert solution.equalFrequency("abcc")
assert not solution.equalFrequency("aazz")
