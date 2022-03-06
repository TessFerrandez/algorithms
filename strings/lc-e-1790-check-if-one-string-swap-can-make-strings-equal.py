'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
'''
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = []
        count = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if count == 2:
                    return False
                count += 1
                diffs.append(i)

        if count == 0:
            return True
        if count == 1:
            return False

        s1_rev = list(s1)
        s1_rev[diffs[0]], s1_rev[diffs[1]] = s1_rev[diffs[1]], s1_rev[diffs[0]]
        return ''.join(s1_rev) == s2


solution = Solution()
assert not solution.areAlmostEqual('attack', 'defend')
assert solution.areAlmostEqual('bank', 'kanb')
assert solution.areAlmostEqual('kelb', 'kelb')
