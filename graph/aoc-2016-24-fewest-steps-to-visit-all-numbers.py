'''
Given a map

###########
#0.1.....2#
#.#######.#
#4.......3#
###########

Part 1: What is the shortest route (starting from 0) to pick up all numbers
----------------------------
Algorithm:
1. Treat all numbers as nodes, build a graph of the shortest path from all nodes to all other nodes
    {0: {1: 2, 2: 8, 3: 10, 4: 2}, 1: ...} - using a BFS shortest path algorithm

2. The distance map now becomes a traveling salesman problem

    Looking at it as a tree - moving from top to bottom

            0
       1    2    3
      2 3  1 3  1 2
      3 2  3 1  2 1

    The shortest distance for traveling to all nodes is g(0, {1, 2, 3, 4}) where
    g(start, other_nodes) = min(dist(start -> node) + g(node, other_nodes - {node}) for node in other_nodes)
    and g(node, {}) = 0

Part 2: What is the shortest route (starting from 0) to pick up all numbers - and return
----------------------------
    Solve the same as above, but g(node, {}) = dist(node, 0) since we have to travel back
'''

from collections import defaultdict, deque


def parse_map(raw_map):
    map = {}
    numbers = {}

    lines = raw_map.splitlines()
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            if ch != '#':
                map[x + y * 1j] = ch
            if '0' <= ch <= '9':
                numbers[ch] = x + y * 1j

    return map, numbers


def get_neighbors(map, current):
    return [current + dir for dir in [-1j, 1, 1j, -1] if (current + dir) in map]


def shortest_path(map, source, dest) -> int:
    todo = deque([(source, 0)])
    visited = set([source])

    if source == dest:
        return 0

    while todo:
        current, distance = todo.popleft()

        for neighbor in get_neighbors(map, current):
            if neighbor == dest:
                return distance + 1

            if neighbor not in visited:
                visited.add(neighbor)
                todo.append((neighbor, distance + 1))

    return -1


def build_distance_graph(map, numbers):
    graph = defaultdict(lambda: {})
    nums = list(numbers.keys())

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            numi, numj = nums[i], nums[j]
            shortest = shortest_path(map, numbers[numi], numbers[numj])
            graph[numi][numj] = shortest
            graph[numj][numi] = shortest

    return graph


def shortest_route(graph, start, others) -> int:
    if not others:
        return 0

    min_cost = float('inf')

    for k in others:
        cost = graph[start][k] + shortest_route(graph, k, others - {k})
        min_cost = min(min_cost, cost)

    return int(min_cost)


def shortest_route_to_pick_up_all(graph):
    keys = set(graph.keys())
    return shortest_route(graph, '0', keys - {'0'})


def shortest_route_and_return(graph, start, others) -> int:
    if not others:
        return graph[start]['0']

    min_cost = float('inf')

    for k in others:
        cost = graph[start][k] + shortest_route_and_return(graph, k, others - {k})
        min_cost = min(min_cost, cost)

    return int(min_cost)


def shortest_route_to_pick_up_all_and_return(graph):
    keys = set(graph.keys())
    return shortest_route_and_return(graph, '0', keys - {'0'})


raw_map = '''###########
#0.1.....2#
#.#######.#
#4.......3#
###########'''

raw_map = open('graph/inputs/2016-24.txt').read().strip()
map, numbers = parse_map(raw_map)
graph = build_distance_graph(map, numbers)
print(shortest_route_to_pick_up_all(graph))
print(shortest_route_to_pick_up_all_and_return(graph))
