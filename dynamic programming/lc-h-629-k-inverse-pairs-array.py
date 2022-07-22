from functools import cache
from itertools import permutations


class Solution:
    # brute force
    def kInversePairs1(self, n: int, k: int) -> int:
        perms = permutations(range(1, n + 1))

        def has_k_pairs(permutation):
            count = 0
            for i in range(len(permutation)):
                for j in range(i + 1, len(permutation)):
                    if permutation[i] > permutation[j]:
                        count += 1
                    if count > k:
                        return False
            return count == k

        total = 0
        for permutation in perms:
            if has_k_pairs(permutation):
                total += 1

        return total

    @cache
    def kInversePairs2(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if k == 0:
            return 1
        inv = 0
        for i in range(min(k, n - 1) + 1):
            inv += self.kInversePairs(n - 1, k - i) % (10 ** 9 + 7)

        return inv

    def kInversePairs(self, n, k):
        MOD = 10 ** 9 + 7
        dp = [0] + [1] * (k + 1)
        for n in range(2, n + 1):
            new = [0]
            for k in range(k + 1):
                v = dp[k + 1]
                v -= dp[k - n + 1] if k >= n else 0
                new.append((new[-1] + v) % MOD)
            dp = new
        return (dp[k + 1] - dp[k]) % MOD


solution = Solution()
assert solution.kInversePairs(3, 0) == 1
assert solution.kInversePairs(3, 1) == 2
