'''
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.
'''
from typing import List
from collections import defaultdict, deque


def build_graph(arr: List[int]):
    indices = defaultdict(list)
    for i, num in enumerate(arr):
        indices[num].append(i)

    arr_len = len(arr)
    graph = defaultdict(set)

    for i, num in enumerate(arr):
        if i > 0:
            graph[i].add(i - 1)
        if i < arr_len - 1:
            graph[i].add(i + 1)
        for ind in indices[num]:
            if ind != i:
                graph[i].add(ind)

    return graph


class Solution:
    # memory limit - for a super big array
    def minJumps1(self, arr: List[int]) -> int:
        arr_len = len(arr)

        if arr_len < 2:
            return 0

        graph = build_graph(arr)

        todo = deque([(0, 0)])
        visited = set()

        while todo:
            current, dist = todo.popleft()

            if current == arr_len - 1:
                return dist

            if current not in visited:
                visited.add(current)

                for neighbor in graph[current]:
                    todo.append((neighbor, dist + 1))

        return -1


    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)

        current = [0]  # current layer
        visited = {0}
        step = 0

        while current:
            next = []

            for node in current:
                if node == n - 1:
                    return step

                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        next.append(child)

                graph[arr[node]].clear()

                for child in [node - 1, node + 1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        next.append(child)

            current = next
            step += 1

        return -1


solution = Solution()
example1 = solution.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404])
assert example1 == 3

example2 = solution.minJumps([7])
assert example2 == 0

example3 = solution.minJumps([7, 6, 9, 6, 9, 6, 9, 7])
assert example3 == 1
