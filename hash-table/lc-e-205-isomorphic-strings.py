class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        used = set()
        mapping = {}

        for i in range(len(s)):
            sch, tch = s[i], t[i]
            if sch not in mapping:
                if tch in used:
                    return False
                mapping[sch] = tch
                used.add(tch)
            else:
                if tch != mapping[sch]:
                    return False
        return True


solution = Solution()
assert solution.isIsomorphic('egg', 'add')
assert not solution.isIsomorphic('foo', 'bar')
assert solution.isIsomorphic('paper', 'title')
