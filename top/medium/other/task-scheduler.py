from typing import Counter, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).most_common()
        max_frequency = counts[0][1]
        max_count = 0

        for _, cnt in counts:
            if cnt == max_frequency:
                max_count += 1
            else:
                break

        part_count = max_frequency - 1
        part_lenght = n - (max_count - 1)
        empty = part_count * part_lenght
        available = len(tasks) - max_frequency * max_count
        idles = max(0, empty - available)

        return len(tasks) + idles


solution = Solution()
assert solution.leastInterval(["A","A","A","B","B","B"], 2) == 8
assert solution.leastInterval(["A","A","A","B","B","B"], 0) == 6
assert solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16
