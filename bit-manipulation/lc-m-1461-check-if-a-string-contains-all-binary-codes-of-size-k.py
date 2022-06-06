class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        visited = set()
        for i in range(len(s) - k + 1):
            visited.add(s[i: i + k])

        print(visited)
        return len(visited) == 2 ** k


solution = Solution()
assert solution.hasAllCodes("00110110", 2)
assert solution.hasAllCodes("0110", 1)
assert not solution.hasAllCodes("0110", 2)
assert solution.hasAllCodes("00110", 2)
