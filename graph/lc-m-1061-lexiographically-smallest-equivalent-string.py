class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ch_map = [i for i in range(26)]

        def find(ch):
            if ch_map[ch] == ch:
                return ch

            ch_map[ch] = find(ch_map[ch])
            return ch_map[ch]

        def union(ch1, ch2):
            ch1 = find(ch1)
            ch2 = find(ch2)
            if ch1 == ch2:
                return
            if ch1 < ch2:
                ch_map[ch2] = ch1
            else:
                ch_map[ch1] = ch2

        for ch1, ch2 in zip(list(s1), list(s2)):
            union(ord(ch1) - ord('a'), ord(ch2) - ord('a'))

        result = ''.join(chr(ord('a') + find(ord(ch) - ord('a'))) for ch in baseStr)
        return result


solution = Solution()
assert solution.smallestEquivalentString('parker', 'morris', 'parser') == 'makkek'
assert solution.smallestEquivalentString('hello', 'world', 'hold') == 'hdld'
assert solution.smallestEquivalentString('leetcode', 'programs', 'sourcecode') == 'aauaaaaada'
