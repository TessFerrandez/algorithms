class Solution:
    # my solution TLE
    def sumScores1(self, s: str) -> int:
        n = len(s)

        def get_prefix(i):
            count = 0
            for j in range(n - i):
                if s[j] == s[i + j]:
                    count += 1
                else:
                    return count
            return count

        first = s[0]
        total = 0
        for i, ch in enumerate(s):
            if ch == first:
                total += get_prefix(i)

        return total

    # winners solution using a z-function
    # see https://cp-algorithms.com/string/z-function.html
    def sumScores2(self, s: str) -> int:
        prefixes = [len(s)]
        left, right = -1, -1

        for i in range(1, len(s)):
            if i <= right and prefixes[i - left] < right - i + 1:
                prefixes.append(prefixes[i - left])
            else:
                left = i
                right = i if (i > right) else right + 1
                while right < len(s) and s[right - i] == s[right]:
                    right += 1
                prefixes.append(right - left)
                right -= 1

        prefixes.append(0)
        return sum(prefixes)

    # example with trivial z-function O(n2) - TLE
    def sumScores(self, s: str) -> int:
        def z_function(s):
            n = len(s)
            z = [0] * n
            for i in range(1, n):
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
            return z

        return sum(z_function(s) + [0]) + len(s)


solution = Solution()
print(solution.sumScores('babab'))
print(solution.sumScores('azbazbzaz'))
print(solution.sumScores('a' * (10 ** 5)))
