# https://www.spoj.com/problems/MARYBMW/
from math import inf
from collections import defaultdict
from heapq import heappop, heappush


def max_speed(n, speeds):
    # create a maximum spanning tree
    graph = defaultdict(list)

    for a, b, speed in speeds:
        graph[a].append([b, -speed])
        graph[b].append([a, -speed])

    msp = defaultdict(list)
    explored = set()
    unexplored = [(0, 1, -1)]

    while unexplored:
        speed, winner, from_city = heappop(unexplored)
        if winner not in explored:
            explored.add(winner)
            if winner != -1 and from_city != -1:
                msp[from_city].append([winner, -speed])
                msp[winner].append([from_city, -speed])

            for neighbor, speed in graph[winner]:
                if neighbor not in explored:
                    heappush(unexplored, (speed, neighbor, winner))

    visited = set()

    def dfs(city, min_speed):
        visited.add(city)
        if city == n:
            return min_speed

        max_speed = 0
        for neighbor, speed in msp[city]:
            if neighbor not in visited:
                max_speed = max(max_speed, dfs(neighbor, min(speed, min_speed)))

        return max_speed

    return dfs(1, inf)


assert max_speed(4, [[1, 2, 80], [3, 1, 20], [2, 3, 60], [4, 3, 300], [2, 4, 90]]) == 80
