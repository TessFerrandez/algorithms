from typing import Counter, List


class Solution:
    def findOriginalArray1(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []

        result = []
        counts = Counter(changed)
        if counts[0] % 2 == 1:
            return []

        for key in sorted(counts.keys(), reverse=True):
            if counts[key] == 0:
                continue
            if key % 2 == 1:
                return []
            half = key // 2
            if half not in counts or counts[half] < counts[key]:
                return []
            num_nums = counts[key]
            counts[key] = 0
            counts[half] -= num_nums
            if key == 0:
                num_nums = num_nums // 2
            for _ in range(num_nums):
                result.append(half)

        return result

    # optimized
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counts = Counter(changed)
        if counts[0] % 2 == 1:
            return []
        for num in sorted(counts):
            if counts[num] > counts[num * 2]:
                return []
            counts[2 * num] -= counts[num] if num != 0 else counts[num] // 2
        return list(counts.elements())


solution = Solution()
assert solution.findOriginalArray([0, 0, 0, 0]) == [0, 0]
assert solution.findOriginalArray([1,3,4,2,6,8]) == [1, 3, 4]
assert solution.findOriginalArray([6, 3, 0, 1]) == []
assert solution.findOriginalArray([1]) == []
