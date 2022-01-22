'''
You are given a 0-indexed 2D integer array grid of size m x n that represents a map of the items in a shop. The integers in the grid represent the following:

0 represents a wall that you cannot pass through.
1 represents an empty cell that you can freely move to and from.
All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.
It takes 1 step to travel between adjacent grid cells.

You are also given integer arrays pricing and start where pricing = [low, high] and start = [row, col] indicates that you start at the position (row, col) and are interested only in items with a price in the range of [low, high] (inclusive). You are further given an integer k.

You are interested in the positions of the k highest-ranked items whose prices are within the given price range. The rank is determined by the first of these criteria that is different:

Distance, defined as the length of the shortest path from the start (shorter distance has a higher rank).
Price (lower price has a higher rank, but it must be in the price range).
The row number (smaller row number has a higher rank).
The column number (smaller column number has a higher rank).
Return the k highest-ranked items within the price range sorted by their rank (highest to lowest). If there are fewer than k reachable items within the price range, return all of them.
'''
from typing import List
from collections import deque


def get_neighbors(row, col, graph):
    neighbors = []
    if (row + 1, col) in graph:
        neighbors.append((row + 1, col))
    if (row - 1, col) in graph:
        neighbors.append((row - 1, col))
    if (row, col + 1) in graph:
        neighbors.append((row, col + 1))
    if (row, col - 1) in graph:
        neighbors.append((row, col - 1))
    return neighbors


def get_distances(graph, start):
    distances = {(start[0], start[1]): 0}

    todo = deque([(start[0], start[1], 0)])

    while todo:
        row, col, dist = todo.popleft()

        for nrow, ncol in get_neighbors(row, col, graph):
            if (nrow, ncol) not in distances:
                distances[(nrow, ncol)] = dist + 1
                todo.append((nrow, ncol, dist + 1))

    return distances


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        graph = {}
        for y, row in enumerate(grid):
            for x, price in enumerate(row):
                if price > 0:
                    graph[(y, x)] = price

        low, high = pricing
        distances = get_distances(graph, start)
        possible = []
        for row, col in graph:
            if (row, col) in distances and low <= graph[(row, col)] <= high:
                possible.append((distances[(row, col)], graph[(row, col)], row, col))

        possible = sorted(possible)
        return [[p[2], p[3]] for p in possible[:k]]


solution = Solution()
print(solution.highestRankedKItems([[2, 0, 3],[2, 0, 3],[2, 0, 3]], [2, 3], [0, 0], 6))
print(solution.highestRankedKItems([[1,2,0,1],[1,3,0,1],[0,2,5,1]], [2,5], [0,0], 3))
