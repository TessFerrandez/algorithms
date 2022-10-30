from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sn, pn = len(s), len(p)
        desired = Counter(p)
        self.to_complete = len(desired)

        def add_letter(ch):
            if ch in desired:
                desired[ch] -= 1
                if desired[ch] == 0:
                    self.to_complete -= 1
                elif desired[ch] == -1:
                    self.to_complete += 1

        def remove_letter(ch):
            if ch in desired:
                desired[ch] += 1
                if desired[ch] == 0:
                    self.to_complete -= 1
                elif desired[ch] == 1:
                    self.to_complete += 1

        good_indices = []

        # look at first word
        for ch in s[:pn]:
            add_letter(ch)

        if self.to_complete == 0:
            good_indices.append(0)

        for i in range(1, sn - pn + 1):
            remove_letter(s[i - 1])
            add_letter(s[i + pn - 1])
            if self.to_complete == 0:
                good_indices.append(i)

        return good_indices


solution = Solution()
assert solution.findAnagrams("abab", "ab") == [0, 1, 2]
assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
