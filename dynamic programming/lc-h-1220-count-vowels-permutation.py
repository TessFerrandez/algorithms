from collections import defaultdict


class Solution:
    def countVowelPermutation1(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        next_ch = {'a': 'e', 'e': 'ai', 'i': 'aeou', 'o': 'iu', 'u': 'a'}
        total = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

        for _ in range(1, n):
            new_total = defaultdict(int)
            for ch in next_ch:
                for next in next_ch[ch]:
                    new_total[next] = (new_total[next] + total[ch]) % MOD
            total = new_total

        return sum(total.values()) % MOD

    # alternative
    def countVowelPermutation(self, n: int) -> int:
        chars = [1, 1, 1, 1, 1]
        MOD = 10 ** 9 + 7

        for _ in range(1, n):
            new_chars = [0] * 5
            new_chars[0] = (chars[1] + chars[2] + chars[4]) % MOD
            new_chars[1] = (chars[0] + chars[2]) % MOD
            new_chars[2] = (chars[1] + chars[3]) % MOD
            new_chars[3] = chars[2] % MOD
            new_chars[4] = (chars[2] + chars[3]) % MOD
            chars = new_chars

        return sum(chars) % MOD


solution = Solution()
assert solution.countVowelPermutation(1) == 5
assert solution.countVowelPermutation(2) == 10
assert solution.countVowelPermutation(3) == 19
assert solution.countVowelPermutation(5) == 68
assert solution.countVowelPermutation(144) == 18208803
