class Solution:
    # my submission during contest
    def countTexts1(self, pressedKeys: str) -> int:
        def get_3combos(freq):
            p1, p2, p3 = 1, 2, 4
            base = {1: 1, 2: 2, 3: 4}
            if freq in base:
                return base[freq]

            for _ in range(4, freq + 1):
                total = p1 + p2 + p3
                p1, p2, p3 = p2, p3, total

            return p3

        def get_4combos(freq):
            p1, p2, p3, p4 = 1, 2, 4, 8
            base = {1: 1, 2: 2, 3: 4, 4: 8}
            if freq in base:
                return base[freq]

            for _ in range(5, freq + 1):
                total = p1 + p2 + p3 + p4
                p1, p2, p3, p4 = p2, p3, p4, total

            return p4

        prev_key, freq, keys = -1, 0, []
        pressedKeys += 'a'

        for key in pressedKeys:
            if key == prev_key:
                freq += 1
            else:
                if prev_key != -1:
                    keys.append((prev_key, freq))
                prev_key = key
                freq = 1

        total = 1
        for key, freq in keys:
            combos = get_4combos(freq) if key in '79' else get_3combos(freq)
            total = (total * combos) % (10 ** 9 + 7)

        return total

    # one pass dynamic programming
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10 ** 9 + 7

        dp = [0] * (len(pressedKeys) + 1)
        dp[0] = 1

        for i in range(1, len(pressedKeys) + 1):
            dp[i] = dp[i - 1] % mod
            if i - 2 >= 0 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                dp[i] = (dp[i] + dp[i - 2]) % mod
                if i - 3 >= 0 and pressedKeys[i - 1] == pressedKeys[i - 3]:
                    dp[i] = (dp[i] + dp[i - 3]) % mod
                    if pressedKeys[i - 1] in '79' and i - 4 >= 0 and pressedKeys[i - 1] == pressedKeys[i - 4]:
                        dp[i] = (dp[i] + dp[i - 4]) % mod
        return dp[-1]


solution = Solution()
assert solution.countTexts('444479999555588866') == 3136
assert solution.countTexts('22233') == 8
assert solution.countTexts('222222222222222222222222222222222222') == 82876089
assert solution.countTexts('355577777788899') == 928
