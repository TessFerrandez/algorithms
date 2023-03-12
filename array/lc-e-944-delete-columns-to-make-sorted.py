from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        to_delete = 0

        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    to_delete += 1
                    break

        return to_delete


solution = Solution()
assert solution.minDeletionSize(["cba","daf","ghi"]) == 1
assert solution.minDeletionSize(["a","b"]) == 0
assert solution.minDeletionSize(["zyx","wvu","tsr"]) == 3
