from collections import defaultdict
from typing import List


class Solution:
    # my solution
    def matchReplacement1(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        ch_map = defaultdict(set)
        for fr, to in mappings:
            ch_map[fr].add(to)
        for ch in sub:
            ch_map[ch].add(ch)

        def is_match(sub_string):
            for i, ch in enumerate(sub_string):
                if ch not in ch_map[sub[i]]:
                    return False
            return True

        s_map = defaultdict(list)
        for i, ch in enumerate(s):
            s_map[ch].append(i)

        possible_starters = []
        for option in ch_map[sub[0]]:
            for i in s_map[option]:
                possible_starters.append(i)

        n = len(s)
        n_sub = len(sub)
        for start in possible_starters:
            if start + n_sub > n:
                continue
            if is_match(s[start: start + n_sub]):
                return True

        return False

    # cleaner
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        ch_map = defaultdict(set)

        for fr, to in mappings:
            ch_map[fr].add(to)

        n = len(sub)
        for i in range(len(s) - n + 1):
            is_match = True
            for s_char, sub_char in zip(s[i: i + n], sub):
                if s_char == sub_char or s_char in ch_map[sub_char]:
                    continue
                else:
                    is_match = False
                    break
            if is_match:
                return True
        return False


solution = Solution()
assert solution.matchReplacement("fool3e7bar", "leet", [["e","3"],["t","7"],["t","8"]])
assert not solution.matchReplacement("fooleetbar", "f00l", [["o","0"]])
assert solution.matchReplacement("Fool33tbaR", "leetd", [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]])
