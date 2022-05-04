class Solution:
    def appealSum(self, s: str) -> int:
        '''
        The appeal of all substrings that end at the ith position is:
        - same as the appeal of all substrings that end at i - 1 plus
        - # of substrings ending at i that do not contain the s[i] character

        0   1   2   3       4
        a   b   c   a       b
        1   1+2 3+3 6+(3-0) 9+(4-1)
        1   3   6   9       12      => total 31

        EX abcab
        index   substrings                              appeal
        0       a(1)                                    1
        1       ab(2), b(1)                             1 + 2 = 3
        2       abc(3), bc(2), c(1)                     3 + 3 = 6
        3       abca(3), bca(3), ca(2), a(1)            6 + 3 = 9
        4       abcab(3), bcab(3), cab(3), ab(2), b(1)  9 + 3 = 12

        pattern:
        if seen s[i] before => prev + (index - last_seen_index)
        else => prev + (index + 1)
        '''
        result, current = 0, 0
        prev = {}

        for i, ch in enumerate(s):
            current += i - (prev[ch] if ch in prev else -1)
            prev[s[i]] = i
            result += current

        return result


solution = Solution()
assert solution.appealSum('abbca') == 28
assert solution.appealSum('code') == 20
