from collections import defaultdict


def matches(d1, d2):
    for d in d1:
        if d1[d] != d2[d]:
            return False
    return True


class Solution:
    # sorting
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        s1_sort = sorted(s1)
        s1_len = len(s1)

        for i in range(len(s2) - s1_len + 1):
            if sorted(s2[i: i + s1_len]) == s1_sort:
                return True

        return False

    # using dict - time limit exceeded
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)

        if s1_len > len(s2):
            return False

        s1map = defaultdict(int)
        for ch in s1:
            s1map[ch] += 1

        for i in range(len(s2) - s1_len + 1):
            s2map = defaultdict(int)
            substr = s2[i: i + s1_len]

            for ch in substr:
                s2map[ch] += 1

            if matches(s1map, s2map):
                return True

        return False

    # using array
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len:
            return False

        s1map = [0 for _ in range(26)]
        for ch in s1:
            s1map[ord(ch) - ord('a')] += 1

        for i in range(len(s2) - s1_len + 1):
            s2map = [0 for _ in range(26)]
            substr = s2[i: i + s1_len]

            for ch in substr:
                s2map[ord(ch) - ord('a')] += 1

            if s1map == s2map:
                return True

        return False


solution = Solution()
assert solution.checkInclusion('adc', 'dcda') == True
assert solution.checkInclusion('ab', 'eidbaooo') == True
assert solution.checkInclusion('ab', 'eidboaoo') == False
