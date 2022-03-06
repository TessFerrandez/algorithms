'''
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
'''
from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        fr_node = defaultdict(list)
        to_node = defaultdict(list)

        for fr, to in connections:
            fr_node[to].append(fr)
            to_node[fr].append(to)

        todo = deque([0])
        done = set([0])
        moves = 0

        while todo:
            node = todo.popleft()
            for neighbor in fr_node[node]:
                if neighbor not in done:
                    done.add(neighbor)
                    todo.append(neighbor)
            for neighbor in to_node[node]:
                if neighbor not in done:
                    moves += 1
                    done.add(neighbor)
                    todo.append(neighbor)

        return moves


solution = Solution()
assert solution.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]) == 3
assert solution.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]) == 2
assert solution.minReorder(3, [[1,0], [2,0]]) == 0
