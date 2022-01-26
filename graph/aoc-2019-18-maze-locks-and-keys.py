'''
[Atribution: Code is heavily borrowed from moltenfire's solution
 https://topaz.github.io/paste/#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]

Given a maze - where @ is the start position,
a-z are keys and A-Z are doors opened by those keys

What is the shortest path - starting at @ to pick up
all keys?

########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################

In part 2 - we modify the map to deploy 4 droids
so the mab below becomes

#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba...BcIJ#
#####.@.#####
#nK.L...G...#
#M###N#H###.#
#o#m..#i#jk.#
#############

#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba@#@BcIJ#
#############
#nK.L@#@G...#
#M###N#H###.#
#o#m..#i#jk.#
#############

Algorithm:
-----------------
If we go through the maze with some normal BFS/Djikstra etc.
there is a huge amount of combinations of different positions and different
existing keys, so we have to greatly reduce the space.

OPTIMIZATION 1: REDUCE THE SPACE TO ONLY A GRAPH BETWEEN KEYS
----------------------------------------------------------------
The only interesting positions in the maze are the positions where we pick up
keys - so we can make another graph - where the node are key positions, and the
edges between them are the distances + the keys. This graph has an edge between
any key and any other key, and from the start position to the keys, but not back.

We can find the distances for the graph using a BFS/djikstra etc. or using the
methods of the networkx library.

Then we can run a BFS, djikstra, or something else on this reduced graph to find
the shortest path, with the target being a full set of keys.

OPTIMIZAION 2: STORE EVERYTHING AS BIT MASKS
----------------------------------------------------------------
To optimize this a bit, we don't want to store our keyring as ['e', 'b', 'a']
- it is much more optimal to store it as a bit mask (10011), the same with our
current state (in part 2 we need to store the current state of 4 droids, ex. if
they are just picking up the keys a, b, e, f the state would be (110011) starting at the tail with a)

To allow for the droids as well, we reserve n bottom bits for droids (n = 1 in part 1 and n = 4 in
part 2) so key a actually is encoded as 10 in part 1 and 10000 in part 2

Bit-masking them allows us to easily compare to see if we have the required keys.

FINDING THE SHORTEST PATH IN THE RESULTING GRAPH
------------
The final search algo is pretty standard (BFS) but we need to record all full paths and take the shortest

state:      position(s) (bit), keys (bit), length
visited:    dict (pos, keys): shortest_paths

todo: our queue of next states to explore

while todo:
    get (pos, keys, length) from todo   # fifo (BFS)

    - if this path is longer than any other path to pos with the given keys
        - move on (this is not interesting)
    - else
        - for all possible next states (next keys we can get to)
            - if they denote a shorter path to a state - record it
                - if we have picked up all keys
                    - record the full path length
                - else
                    - add the next states to todo to explore

The answer is the shortest of the full path lengths
'''

from collections import defaultdict, deque
from itertools import combinations
import networkx as nx


class Path():
    def __init__(self, current_nodes, collected_keys, distance) -> None:
        self.current_nodes = current_nodes
        self.collected_keys = collected_keys
        self.distance = distance

    def get_state(self):
        return (self.current_nodes, self.collected_keys)

    def get_num_keys(self):
        return bin(self.collected_keys).count('1')

    def __repr__(self) -> str:
        return str(self.current_nodes) + ' ' + bin(self.collected_keys) + ' ' + self.distance

    def __str__(self) -> str:
        return str(self.current_nodes) + ' ' + bin(self.collected_keys) + ' ' + self.distance


def parse_maze(raw_map, part2=False):
    maze = defaultdict(int)
    keys = {}
    doors = {}
    droids = []

    rows = [list(row) for row in raw_map.strip().splitlines()]

    if part2:
        mid_y, mid_x = (len(rows) - 1) // 2, (len(rows[0]) - 1) // 2
        rows[mid_y - 1][mid_x - 1: mid_x + 2] = "@#@"
        rows[mid_y][mid_x - 1: mid_x + 2] = "###"
        rows[mid_y + 1][mid_x - 1: mid_x + 2] = "@#@"

    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c != '#':
                pos = x + y * 1j
                maze[pos] = 1
                if c == '@':
                    droids.append(pos)
                elif 'a' <= c <= 'z':
                    keys[ord(c) - 97] = pos
                elif 'A' <= c <= 'Z':
                    doors[ord(c) - 65] = pos

    num_droids = len(droids)
    keys = {key + num_droids: pos for key, pos in keys.items()}
    doors = {key + num_droids: pos for key, pos in doors.items()}
    return maze, keys, doors, droids


def build_maze_graph(map):
    edges = []

    for pos in map:
        for neighbor in [pos + d for d in [-1j, 1, 1j, -1]]:
            if neighbor in map:
                edges.append((pos, neighbor))

    return nx.Graph(edges)


def get_distance(graph, pos1, pos2, doors):
    if not nx.has_path(graph, pos1, pos2):
        return -1, 0

    path = nx.shortest_path(graph, pos1, pos2)
    path_set = set(path)
    doors_in_way = 0

    for door, door_pos in doors.items():
        if door_pos in path_set:
            doors_in_way += (1 << door)

    distance = len(path) - 1
    return distance, doors_in_way


def build_key_to_key_graph(maze, keys, doors, droids, droid_nums):
    maze_graph = build_maze_graph(maze)

    key_to_key_graph = defaultdict(dict)
    key_to_bits = {key: 1 << key for key in keys.keys()}

    for droid_pos, droid_num in zip(droids, droid_nums):
        droid_bits = 1 << droid_num
        for key, key_pos in keys.items():
            key_bits = key_to_bits[key]
            distance, doors_in_way = get_distance(maze_graph, droid_pos, key_pos, doors)
            if distance != -1:
                key_to_key_graph[droid_bits][key_bits] = (distance, doors_in_way)

    for key1, key2 in combinations(keys.keys(), 2):
        key1_bits = key_to_bits[key1]
        key2_bits = key_to_bits[key2]

        distance, doors_in_way = get_distance(maze_graph, keys[key1], keys[key2], doors)
        if distance != -1:
            key_to_key_graph[key1_bits][key2_bits] = (distance, doors_in_way)
            key_to_key_graph[key2_bits][key1_bits] = (distance, doors_in_way)

    return dict(key_to_key_graph)


def find_next_possible_states(key_to_key_graph, current_nodes, collected_keys, current_distance):
    '''
    go through all the key to key combos
    - for all the keys that we are currently on (ex. if we stand on key a, b, c, d)
    - look at all the next keys that we haven't already picked up
    - if we can reach them, without going through a locked door that we don't have a key to
    - this is a possible next state
    '''
    for key1, key1_info in key_to_key_graph.items():
        if key1 & current_nodes:                                        # if key1 in current nodes
            for key2, key2_info in key1_info.items():
                if not key2 & collected_keys:                           # and key2 not in collected keys
                    distance, doors_in_way = key2_info
                    if doors_in_way & collected_keys == doors_in_way:   # and we don't have any locked doors between
                        new_positions = current_nodes ^ key1 | key2     # this is a new valid state
                        yield (new_positions, collected_keys + key2, current_distance + distance)


def find_shortest_path(maze, keys, doors, droids):
    total_keys = len(keys)

    num_droids = len(droids)
    droid_nums = list(range(num_droids))

    key_to_key_graph = build_key_to_key_graph(maze, keys, doors, droids, droid_nums)

    shortest_full_path_length = 10 ** 6
    shortest_paths = defaultdict(int)

    start = 2 ** num_droids - 1             # 1 if single droid, 1111 if 4 droids (e.g. 1000 + 100 + 10 + 1)
    todo = deque([(start, 0, 0)])           # all droids, no keys, 0 steps

    while todo:
        current_nodes, collected_keys, current_path_length = todo.popleft()

        # if we already have a shorter path, don't bother
        if shortest_paths[(current_nodes, collected_keys)] < current_path_length:
            continue

        for new_nodes, new_collected_keys, new_path_length in find_next_possible_states(key_to_key_graph, current_nodes, collected_keys, current_path_length):
            state = (new_nodes, new_collected_keys)

            # if we have a new shortest path
            if (state in shortest_paths and new_path_length < shortest_paths[state]) or state not in shortest_paths:

                # save the path_length
                shortest_paths[state] = new_path_length

                if bin(new_collected_keys).count('1') == total_keys:
                    # if we have found all our keys - record the shortest path
                    shortest_full_path_length = min(shortest_full_path_length, new_path_length)
                else:
                    # else add this state to the ones we want to explore
                    todo.append((new_nodes, new_collected_keys, new_path_length))

    return shortest_full_path_length


raw_map = '''#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba...BcIJ#
#####.@.#####
#nK.L...G...#
#M###N#H###.#
#o#m..#i#jk.#
#############'''

raw_map2 = '''########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################'''

# raw_map = open('graph/inputs/2019-18.txt').read()

# Part 1
maze, keys, doors, droids = parse_maze(raw_map)
min_length = find_shortest_path(maze, keys, doors, droids)
print("Part 1:", min_length)

# Part 2
maze, keys, doors, droids = parse_maze(raw_map, part2=True)
min_length = find_shortest_path(maze, keys, doors, droids)
print("Part 2:", min_length)
