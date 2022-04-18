from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        queue = []

        while people:
            person = people.pop()
            queue.insert(person[1], person)

        return queue


solution = Solution()
assert solution.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
assert solution.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]) == [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
