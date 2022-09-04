from collections import defaultdict
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        diffs = defaultdict(list)
        for i in range(10):
            if i + k < 10:
                diffs[i].append(i + k)
            if i - k >= 0:
                diffs[i].append(i - k)

        old_nums = {num: [str(num)] for num in range(10)}

        for i in range(2, n + 1):
            nums = defaultdict(list)
            for j in range(10):
                for diff in diffs[j]:
                    for old_str in old_nums[diff]:
                        nums[j].append(str(j) + old_str)

            old_nums = nums

        results = set()
        for num in old_nums:
            for s in old_nums[num]:
                if not s.startswith('0'):
                    results.add(int(s))

        return list(results)


solution = Solution()
assert sorted(solution.numsSameConsecDiff(3, 7)) == [181, 292, 707, 818, 929]
assert sorted(solution.numsSameConsecDiff(2, 1)) == [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
assert sorted(solution.numsSameConsecDiff(2, 0)) == [11,22,33,44,55,66,77,88,99]
