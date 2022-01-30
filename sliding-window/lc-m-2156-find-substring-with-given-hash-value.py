'''
The hash of a 0-indexed string s of length k, given integers p and m, is computed using the following function:

hash(s, p, m) = (val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1) mod m.
Where val(s[i]) represents the index of s[i] in the alphabet from val('a') = 1 to val('z') = 26.

You are given a string s and the integers power, modulo, k, and hashValue. Return sub, the first substring of s of length k such that hash(sub, power, modulo) == hashValue.

The test cases will be generated such that an answer always exists.

A substring is a contiguous non-empty sequence of characters within a string.
'''
class Solution:
    # time limit exceeded
    def subStrHash1(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        hash = sum((ord(s[j]) - 96) * (power ** j) for j in range(k))
        last_pow = power ** (k - 1)

        if hash % modulo == hashValue:
            return s[:k]

        for i in range(1, len(s) - k + 1):
            hash = (hash - (ord(s[i - 1]) - 96)) // power + (ord(s[i + k - 1]) - 96) * last_pow
            if hash % modulo == hashValue:
                return s[i: i + k]

        return ''

    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c) - 96

        res = n = len(s)
        pk = pow(power, k, modulo)
        hash = 0

        for i in range(n - 1, -1, -1):
            hash = (hash * power + val(s[i])) % modulo
            if i + k < n:
                hash = (hash - val(s[i + k]) * pk) % modulo
            if hash == hashValue:
                res = i

        return s[res: res + k]


solution = Solution()
print(solution.subStrHash('xxterzixjqrghqyeketqeynekvqhc', 15, 94, 4, 16))
print(solution.subStrHash('xmmhdakfursinye', 96, 45, 15, 21))
print(solution.subStrHash('leetcode', 7, 20, 2, 0))
print(solution.subStrHash('fbxzaad', 31, 100, 3, 32))
