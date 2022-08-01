from collections import defaultdict
from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        count_p = Counter(p)
        to_fill, complete = len(count_p), 0

        result = []

        count_s = defaultdict(int)
        for ch in s[:p_len]:
            count_s[ch] += 1
            if ch in count_p and count_s[ch] == count_p[ch]:
                complete += 1
        if complete == to_fill:
            result.append(0)

        for i in range(s_len - p_len):
            # remove the last character
            last = s[i]
            if last in count_p and count_s[last] == count_p[last]:
                complete -= 1
            count_s[last] -= 1

            # add the next new characters
            next = s[i + p_len]
            count_s[next] += 1
            if next in count_p and count_s[next] == count_p[next]:
                complete += 1

            # if we have a full set of complete characters
            # mark as found
            if complete == to_fill:
                result.append(i + 1)

        return result


solution = Solution()
assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
assert solution.findAnagrams("abab", "ab") == [0, 1, 2]
