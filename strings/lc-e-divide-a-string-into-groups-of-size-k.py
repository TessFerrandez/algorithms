from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        s += fill * k

        result = []
        for i in range(0, n, k):
            result.append(s[i: i + k])
        return result


solution = Solution()
assert solution.divideString("abcdefghi", 3, "x") == ["abc", "def", "ghi"]
assert solution.divideString("abcdefghij", 3, "x") == ["abc", "def", "ghi", "jxx"]
