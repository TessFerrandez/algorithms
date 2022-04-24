from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        required = Counter(t)
        required_chars = len(required)

        left, right = 0, 0
        complete = 0
        window = defaultdict(int)

        results = float("inf"), None, None

        while right < len(s):
            ch = s[right]
            window[ch] += 1

            if ch in required and window[ch] == required[ch]:
                complete += 1

            while left <= right and complete == required_chars:
                ch = s[left]

                if right - left + 1 < results[0]:
                    results = (right - left + 1, left, right)

                window[ch] -= 1
                if ch in required and window[ch] < required[ch]:
                    complete -= 1

                left += 1

            right += 1

        return "" if results[0] == float("inf") else s[results[1]: results[2] + 1]


solution = Solution()
assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert solution.minWindow("a", "a") == "a"
assert solution.minWindow("a", "aa") == ""
