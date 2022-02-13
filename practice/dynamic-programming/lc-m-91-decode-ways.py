class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {'': 1}

        def num_decodings(s):
            if s in cache:
                return cache[s]

            if s[0] == '0':
                return 0
            num_ways = num_decodings(s[1:])
            if s[0] == '1' and len(s) > 1:
                num_ways += num_decodings(s[2:])
            elif s[0] == '2' and len(s) > 1 and '0' <= s[1] <= '6':
                num_ways += num_decodings(s[2:])
            cache[s] = num_ways
            return num_ways

        return num_decodings(s)


solution = Solution()
assert solution.numDecodings('11106') == 2
assert solution.numDecodings('12') == 2
assert solution.numDecodings('226') == 3
assert solution.numDecodings('06') == 0
