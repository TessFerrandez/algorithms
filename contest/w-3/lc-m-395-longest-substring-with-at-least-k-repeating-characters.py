from collections import Counter, defaultdict


class Solution:
    # TLE
    def longestSubstring_tle(self, s: str, k: int) -> int:
        if s == '' or k > len(s):
            return 0

        n = len(s)
        result = 0
        for start in range(n):
            for end in range(start, n):
                counts = Counter(s[start: end + 1])
                if min(counts.values()) < k:
                    continue
                result = max(result, end - start + 1)

        return result

    # divide and conquer
    def longestSubstring2(self, s: str, k: int) -> int:
        def longest(s, k):
            if len(s) < k:
                return 0

            counts = Counter(s)

            for mid in range(len(s)):
                if counts[s[mid]] >= k:
                    continue

                next_mid = mid + 1

                while next_mid < len(s) and counts[s[next_mid]] < k:
                    next_mid += 1

                return max(longest(s[: mid], k), longest(s[next_mid:], k))

            return len(s)

        return longest(s, k)

    # two pointer
    def longestSubstring1(self, s: str, k: int) -> int:
        total_unique = len(set(list(s)))
        result = 0

        for curr_unique in range(1, total_unique + 1):
            counts = defaultdict(int)
            start, end, unique, count_at_least_k = 0, 0, 0, 0

            while end < len(s):
                if unique <= curr_unique:
                    # expand window
                    if counts[s[end]] == 0:
                        unique += 1
                    counts[s[end]] += 1
                    if counts[s[end]] == k:
                        count_at_least_k += 1
                    end += 1
                else:
                    # shrink window
                    if counts[s[start]] == k:
                        count_at_least_k -= 1
                    counts[s[start]] -= 1
                    if counts[s[start]] == 0:
                        unique -= 1
                    start += 1

                if unique == curr_unique and unique == count_at_least_k:
                    result = max(end - start, result)

        return result

    def longestSubstring(self, s: str, k: int) -> int:
        if s == '':
            return 0

        counts = Counter(s)
        if min(counts.values()) >= k:
            return len(s)

        sub_str = ''
        result = 0
        for ch in s:
            if counts[ch] >= k:
                sub_str += ch
            else:
                if sub_str != '':
                    result = max(result, self.longestSubstring(sub_str, k))
                sub_str = ''
            result = max(result, self.longestSubstring(sub_str, k))
        return result


solution = Solution()
assert solution.longestSubstring('ababbc', 2) == 5
assert solution.longestSubstring('ababcabaaadc', 2) == 4
assert solution.longestSubstring('aaabb', 3) == 3
