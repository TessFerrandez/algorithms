'''
given a grid of risk-levels:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581

Get from the top/left to bottom/right with
as little risk as possible. You take on a risk
as you move TO a new position.

Diagonal moves are not allowed

Algorithm: this is a graph with weighted edges
so we need an algorithm like djikstra to find the
path with the lowest cost

ex. 3x3 top in the above grid would be
ABC
DEF
GHI

We could build a graph like the below and
let networkx do the job

{A: {B: 1, D: 1}, B: {A: 1, C: 6, E: 3} ...}

Or build our own djikstra, reading neighbors as we go along
'''
from collections import defaultdict
from queue import PriorityQueue


def build_graph(raw_grid):
    lines = raw_grid.splitlines()
    grid = [[int(d) for d in row]
            for row in lines]
    width, height = len(grid[0]), len(grid)
    graph = defaultdict(dict)
    for y in range(height):
        for x in range(width):
            if y > 0:
                graph[(x, y)][(x, y - 1)] = grid[y - 1][x]
            if y < height - 1:
                graph[(x, y)][(x, y + 1)] = grid[y + 1][x]
            if x > 0:
                graph[(x, y)][(x - 1, y)] = grid[y][x - 1]
            if x < height - 1:
                graph[(x, y)][(x + 1, y)] = grid[y][x + 1]

    return graph, (0, 0), (width - 1, height - 1)


def djikstra(graph, start):
    visited = set()
    previous = {node: None for node in graph}
    costs = {node: 10**9 for node in graph}
    costs[start] = 0

    todo = PriorityQueue()
    todo.put((0, start))

    while not todo.empty():
        current_cost, current = todo.get()
        visited.add(current)

        for neighbor in graph[current]:
            neighbor_cost = graph[current][neighbor]
            if neighbor not in visited:
                old_cost = costs[neighbor]
                new_cost = current_cost + neighbor_cost
                if new_cost < old_cost:
                    previous[neighbor] = current
                    todo.put((new_cost, neighbor))
                    costs[neighbor] = new_cost

    return costs, previous


raw_grid = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''

raw_grid = open('graph/inputs/2021-15.txt').read()
graph, start, end = build_graph(raw_grid)
costs, prev = djikstra(graph, start)
print('Part 1:', costs[end])
