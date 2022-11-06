class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))


solution = Solution()
assert solution.orderlyQueue("cba", 1) == "acb"
assert solution.orderlyQueue("baaca", 3) == "aaabc"
