class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        current = [(i, i) for i in range(n)]
        for i in range(n - 1):
            if s[i + 1] == s[i]:
                current.append((i, i + 1))

        count = len(current)

        while current:
            next = []
            for left, right in current:
                if left - 1 >= 0 and right + 1 < n:
                    if s[left - 1] == s[right + 1]:
                        next.append((left - 1, right + 1))
            count += len(next)
            current = next

        return count


solution = Solution()
assert solution.countSubstrings('abc') == 3
assert solution.countSubstrings('aaa') == 6
