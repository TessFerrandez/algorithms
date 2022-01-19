'''
This is a simplified subset of the code for aoc 2019-18
Where we want to build a graph from every key position
to every other key position - understanding the distance between them
and also the set of keys needed to get there

a-z are keys, A-Z are doors, @ is the droid
bigger problem (shortest path to find all keys)
sub problem solved here (build a key-to-key graph where the edges are distance + keys needed)

########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################

ex. a -> e == 10 steps, need (A, B)
so we build

{a: {b: ..., e: (10, (A, B))}, b: ...}

We can build a networkx graph from all open spaces (including doors, keys etc.)
to it's immediate neigbors that are not walls (build_maze_graph)

Then to find the distance and the keys we can simply use

nx.has_path(graph, pos1, pos2)      -> Returns true if there is a way to go from pos1 to pos2
nx.shortest_path(graph, pos1, pos2) -> Returns the list of nodes we go through, this gives us
                                        - the doors (we can see if the steps are door slots)
                                        - the distance (length of path)

There are many other methods, including djikstra, a*, all shortest paths etc.
https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
'''

from collections import defaultdict
from itertools import combinations
import networkx as nx


def parse_maze(raw_map):
    maze = defaultdict(int)
    keys = {}
    doors = {}
    droid = 0

    rows = [list(row) for row in raw_map.strip().splitlines()]

    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c != '#':
                pos = x + y * 1j
                maze[pos] = 1
                if c == '@':
                    droid = pos
                elif 'a' <= c <= 'z':
                    keys[c] = pos
                elif 'A' <= c <= 'Z':
                    doors[c] = pos

    return maze, keys, doors, droid


def build_maze_graph(maze):
    edges = []

    for pos in maze:
        for neighbor in [pos + d for d in [-1j, 1, 1j, -1]]:
            if neighbor in maze:
                edges.append((pos, neighbor))

    return nx.Graph(edges)


def get_distance(graph, pos1, pos2, doors):
    if not nx.has_path(graph, pos1, pos2):
        return -1, 0

    path = nx.shortest_path(graph, pos1, pos2)
    path_set = set(path)
    doors_in_way = set()

    for door, door_pos in doors.items():
        if door_pos in path_set:
            doors_in_way.add(door)

    distance = len(path) - 1
    return distance, doors_in_way


def build_key_to_key_graph(maze, keys, doors, droid_pos):
    maze_graph = build_maze_graph(maze)

    key_to_key_graph = defaultdict(dict)

    for key, key_pos in keys.items():
        distance, doors_in_way = get_distance(maze_graph, droid_pos, key_pos, doors)
        if distance != -1:
            key_to_key_graph['@'][key] = (distance, doors_in_way)

    for key1, key2 in combinations(keys.keys(), 2):
        distance, doors_in_way = get_distance(maze_graph, keys[key1], keys[key2], doors)
        if distance != -1:
            key_to_key_graph[key1][key2] = (distance, doors_in_way)
            key_to_key_graph[key2][key1] = (distance, doors_in_way)

    return dict(key_to_key_graph)


raw_map = '''########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################'''

# raw_map = open('graph/inputs/2019-18.txt').read().strip()

maze, keys, doors, droid = parse_maze(raw_map)
maze_graph = build_maze_graph(maze)
key_to_key_graph = build_key_to_key_graph(maze_graph, keys, doors, droid)

for key, info in key_to_key_graph.items():
    print(key, info)
