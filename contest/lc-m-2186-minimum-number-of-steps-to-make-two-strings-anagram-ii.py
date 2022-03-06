from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counts = Counter(s)
        t_counts = Counter(t)

        steps = 0
        for ch in s_counts:
            if ch not in t_counts:
                steps += s_counts[ch]
            if ch in t_counts:
                steps += abs(s_counts[ch] - t_counts[ch])
                t_counts[ch] = 0

        for ch in t_counts:
            steps += t_counts[ch]

        return steps


solution = Solution()
assert solution.minSteps('leetcode', 'coats') == 7
assert solution.minSteps('night', 'thing') == 0
