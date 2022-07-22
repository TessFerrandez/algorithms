class Solution:
    def greatestLetter1(self, s: str) -> str:
        lower, upper = set(), set()
        best = ''

        for ch in s:
            if ch.isupper():
                if ch.lower() in lower and ch > best:
                    best = ch
                else:
                    upper.add(ch)
            elif ch.upper() in upper and ch.upper() > best:
                best = ch.upper()
            else:
                lower.add(ch)

        return best

    def greatestLetter(self, s: str) -> str:
        upper = {ch for ch in s if ch.isupper()}
        lower = {ch.upper() for ch in s if ch.islower()}
        common = upper.intersection(lower)

        if not common:
            return ''
        return sorted(common)[0]


solution = Solution()
assert solution.greatestLetter("Aa") == 'A'
assert solution.greatestLetter("lEeTcOdE") == 'E'
assert solution.greatestLetter("arRAzFif") == 'A'
assert solution.greatestLetter("AbCdEfGhIjK") == ''
