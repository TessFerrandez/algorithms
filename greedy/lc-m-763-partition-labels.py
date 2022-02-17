from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        n = len(s)

        for i, ch in enumerate(s):
            last[ch] = i

        if n == 1:
            return [1]

        end = -1
        partitions = []

        while end < n - 1:
            start = end + 1
            end = last[s[start]]
            i = start
            while i <= end:
                if last[s[i]] > end:
                    end = last[s[i]]
                i += 1
            partitions.append(end - start + 1)

        return partitions


solution = Solution()
assert solution.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
assert solution.partitionLabels("qiejxqfnqceocmy") == [13, 1, 1]
