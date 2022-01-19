'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
'''
from typing import List
from collections import defaultdict, deque
from queue import PriorityQueue


class Solution:
    def networkDelayTime1(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        delay = {}

        for o, d, t in times:
            graph[o][d] = t

        todo = deque([(k, 0)])
        while todo:
            node, time = todo.popleft()

            if node in delay:
                continue

            delay[node] = time

            for neighbor in graph[node]:
                todo.append((neighbor, time + graph[node][neighbor]))

        for i in range(1, n + 1):
            if i not in delay:
                return -1

        return max(delay.values())

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)

        for o, d, t in times:
            graph[o][d] = t

        visited = set()
        # previous = {node: None for node in range(1, n + 1)}
        delay = {node: 10 ** 9 for node in range(1, n + 1)}
        delay[k] = 0

        todo = PriorityQueue()
        todo.put((0, k))

        while not todo.empty():
            current_delay, current = todo.get()
            visited.add(current)

            for neighbor in graph[current]:
                neighbor_delay = graph[current][neighbor]
                if neighbor not in visited:
                    old_delay = delay[neighbor]
                    new_delay = current_delay + neighbor_delay
                    if new_delay < old_delay:
                        # previous[neighbor] = current
                        todo.put((new_delay, neighbor))
                        delay[neighbor] = new_delay

        max_delay = max(delay.values())
        if max_delay == 10 ** 9:
            return -1
        return max_delay


solution = Solution()
assert solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
assert solution.networkDelayTime([[1,2,1]], 2, 1) == 1
assert solution.networkDelayTime([[1,2,1]], 2, 2) == -1
assert solution.networkDelayTime([[1,2,1],[2,1,3]], 2, 2) == 3
assert solution.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1) == 3
