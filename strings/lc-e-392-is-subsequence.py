class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)
        if slen == 0:
            return True
        if tlen == 0:
            return False
        if tlen < slen:
            return False

        i, j = 0, 0
        while i < slen and j < tlen:
            while j < tlen and t[j] != s[i]:
                j += 1
            if j < tlen and t[j] == s[i]:
                i += 1
                j += 1

        return i == slen


solution = Solution()
assert solution.isSubsequence('abc', 'ahbgdc') == True
assert solution.isSubsequence('axc', 'ahbgdc') == False
