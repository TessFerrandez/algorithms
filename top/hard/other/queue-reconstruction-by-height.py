from collections import defaultdict
from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    # my solution - TLE
    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        def can_go(prospect, result):
            h, k = prospect

            if k == 0:
                return True

            count = 0
            for hr, _ in result:
                if hr >= h:
                    count += 1
                if count == k:
                    return True

            return False

        before = defaultdict(list)
        for h, k in people:
            before[k].append([h, k])

        heap, result = [], []
        heapify(heap)

        for i in range(len(people)):
            for person in before[i]:
                heappush(heap, person)

            not_possible = []
            prospect = heappop(heap)
            while not can_go(prospect, result):
                not_possible.append(prospect)
                prospect = heappop(heap)

            for p in not_possible:
                heappush(heap, p)

            result.append(prospect)

        return result

    # sort and insert
    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        '''
        Pick tallest, and sort them in a subarray (S) - since none are taller, each persons index will be their k value
        For 2nd tallest group (and the rest), insert them into (S) by k value

        Ex. [7,0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]
        S = [7, 0], [7, 1]
        Add [6, 1] => [7, 0], [6, 1], [7, 1]
        Add [5, 0] [5, 2] => [5, 0], [7, 0], [5, 2], [6, 1], [7, 1]
        '''
        peeps = defaultdict(list)
        result = []

        for person in people:
            height, _ = person
            peeps[height].append(person)

        heights = list(peeps.keys())
        heights.sort(reverse=True)

        for height in heights:
            peeps[height].sort()
            for person in peeps[height]:
                _, k = person
                result.insert(k, person)

        return result

    # sort and insert - much shorter
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        result = []

        for person in people:
            result.insert(person[1], person)

        return result


solution = Solution()
assert solution.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]) == [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
assert solution.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]) == [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
