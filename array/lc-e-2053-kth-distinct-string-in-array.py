from collections import Counter


class Solution(object):
    def kthDistinct(self, arr, k) -> str:
        distinct = [string for string, count in Counter(arr).items() if count == 1]
        if len(distinct) >= k:
            return distinct[k - 1]
        return ""


solution = Solution()
assert solution.kthDistinct(["d", "b", "c", "b", "c", "a"], 2) == "a"
assert solution.kthDistinct(["aaa", "aa", "a"], 1) == "aaa"
assert solution.kthDistinct(["a", "b", "a"], 3) == ""
