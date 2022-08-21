from collections import defaultdict
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count = defaultdict(int)
        for item, weight in items1:
            count[item] = weight
        for item, weight in items2:
            count[item] += weight
        return sorted([[item, count[item]] for item in count])


solution = Solution()
assert solution.mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]) == [[1, 6], [3, 9], [4, 5]]
assert solution.mergeSimilarItems([[1,1],[3,2],[2,3]], [[2,1],[3,2],[1,3]]) == [[1,4],[2,4],[3,4]]
assert solution.mergeSimilarItems([[1,3],[2,2]], [[7,1],[2,2],[1,4]]) == [[1,7],[2,4],[7,1]]
