'''
Given a group of programs that can interact

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5

Part 1: how many programs are in the group containing program 0?
--------------
Depth first search/exploration - recording the size

Part 2: how many groups are there?
--------------
Depth first search/exploration - count fully explored groups
'''
from collections import defaultdict


def get_group_size(graph, current, visited):
    size = 1

    if current in visited:
        return 0

    visited.add(current)

    for neighbor in graph[current]:
        size += get_group_size(graph, neighbor, visited)

    return size


def explore_group(graph, current, visited):
    if current in visited:
        # we've already been here, don't double count
        return False

    visited.add(current)

    # explore neighbors (marking them visited)
    for neighbor in graph[current]:
        explore_group(graph, neighbor, visited)

    # we're done exploring
    return True


def count_groups(graph):
    count = 0
    visited = set()

    for program in graph:
        if explore_group(graph, program, visited):
            count += 1

    return count


def parse_graph(raw_data):
    graph = defaultdict(lambda: set())

    lines = raw_data.splitlines()
    for line in lines:
        p1, p2 = line.split(' <-> ')
        programs = p2.split(', ')
        for program in programs:
            graph[p1].add(program)
            graph[program].add(p1)

    return graph


raw_data = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''

raw_data = open('graph/inputs/2017-12.txt').read().strip()
graph = parse_graph(raw_data)
print("Part 1:", get_group_size(graph, '0', set()))
print("Part 2:", count_groups(graph))
