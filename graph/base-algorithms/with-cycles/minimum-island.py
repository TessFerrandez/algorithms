'''
given a grid - how many islands are there

.#..#.
##..#.
.#....
...##.
.#.##.
......

Here we have 4 islands

This is the same problem as connected-count
where the nodes are (1, 0) for example (land areas)
and neighbors are other land areas (1, 1)

To make things simpler...
store the grid as a dict of only the land areas,
and the key as a complex x + y * 1j
this way we only need to iterate through the land masses
and the neighbors are any neighbors in
(x + y * 1j) + [-1j, 1, 1j, -1] = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
'''
def parse_grid(grid):
    rows = grid.splitlines()
    graph = {}

    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch == "#":
                graph[(x + y * 1j)] = True

    return graph


def explore_land(graph, current, visited):
    size = 1

    if current in visited:
        return 0

    visited.add(current)

    for diff in [-1j, 1, 1j, -1]:
        neighbor = current + diff
        if neighbor in graph:
            size += explore_land(graph, neighbor, visited)

    return size


def minimum_island(graph):
    min_size = float('inf')
    visited = set()

    for land in graph:
        if land not in visited:
            size = explore_land(graph, land, visited)
            min_size = min(min_size, size)

    return min_size


grid = '''.#..#.
##..#.
.#....
...##.
.#.##.
.#....'''

graph = parse_grid(grid)
print(minimum_island(graph))
