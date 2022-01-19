'''
Given bi-directional graph find the number of possible paths from start to end

start-A
start-b
A-c
A-b
b-d
A-end
b-end

Part 1: small caves (b, c, d) can only be visited once, big caves (A) can be visited
unlimited times
------------------
Algorithm: BFS or DFS explore to find all paths, but only add small caves to visited

Part 2: big caves can still be visited unlimited, but for small caves, we can visit
one cave twice, the rest should only be visited maximum once
------------------
Algorithm: Same as before, but when looking at the possible new "neighbors" - if we
want to visit a new small cave, and it has already been visited, check that we haven't
visited any other cave twice
'''
from collections import defaultdict, Counter


def parse_raw(raw_input):
    graph = defaultdict(list)

    for line in raw_input.strip().splitlines():
        fr, to = line.split('-')
        graph[fr].append(to)
        if fr != 'start' and to != 'end':
            graph[to].append(fr)

    return graph


def get_all_paths(graph, start, end):
    def dfs(graph, start, end, visited, path):
        if start.lower() == start:
            visited.add(start)

        path.append(start)

        if start == end:
            paths.append(path.copy())
        else:
            for neighbor in graph[start]:
                if neighbor not in visited:
                    dfs(graph, neighbor, end, visited, path)

        path.pop()
        if start in visited:
            visited.remove(start)

    paths = []
    dfs(graph, start, end, set(), [])
    return paths


def count_visited_twice(path):
    return len([cave for cave, count in Counter([cave for cave in path if cave.islower()]).items() if count > 1])


def count_all_paths(graph, start, end):
    path_count = [0]

    def dfs(graph, start, end, visited):
        if start.lower() == start:
            visited.add(start)

        if start == end:
            path_count[0] += 1
        else:
            for neighbor in graph[start]:
                if neighbor not in visited:
                    dfs(graph, neighbor, end, visited)

        if start in visited:
            visited.remove(start)

    dfs(graph, start, end, set())
    return path_count[0]


def count_all_paths2(graph, start, end):
    def dfs(graph, start, end, visited, path):
        if start.lower() == start:
            visited[start] += 1
        path.append(start)

        if start == end:
            path_count[0] += 1
        else:
            for neighbor in graph[start]:
                if visited[neighbor] == 0 or (visited[neighbor] < 2 and (neighbor.isupper() or count_visited_twice(path) == 0)):
                    dfs(graph, neighbor, end, visited, path)

        path.pop()
        visited[start] -= 1

    path_count = [0]
    visited = defaultdict(int)
    dfs(graph, start, end, visited, [])
    return path_count[0]


raw_input1 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

raw_input2 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''

raw_input3 = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''

raw_input = open('graph/inputs/2021-12.txt').read()
graph = parse_raw(raw_input)
print("Part 1:", count_all_paths(graph, 'start', 'end'))

graph = parse_raw(raw_input)
print("Path 2:", count_all_paths2(graph, 'start', 'end'))
