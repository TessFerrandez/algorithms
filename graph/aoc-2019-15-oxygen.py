'''
A repair droid can given you information about your neighbor tiles (through an int-code program)
Give it a direction [NSWE] and it will return with

0 = WALL
1 = EMPTY (and move forward)
2 = OXYGEN (and move forward)

Part 1:
----------------
What is the minimum number of moves to go to the oxygen tank

Part 2:
----------------
If the oxygen flows at one step per minute - how many minutes does it take to oxygenate the whole world?

Algorithms:
----------------
BUILD MAP

First we need to build the map - since the droid moves when it finds an empty space we can't do
a normal DFS or BFS to explore, as they require you to be able to "teleport" to locations
(the ones you pop from the queue/stack).

We could do this with back-tracking... but turns out we can simply turn right if we hit a wall, and left
if we moved to an empty space, until we're back at the origin. (not entirely sure why)

SHORTEST PATH

For this we use a standard BFS shortest path (since we have the origin and the oxygen location)

OXYGEN FLOW

Here we need to find the longest path... one way to do this is by using the algorithm suggested by the
problem and flood fill. Starting with the oxygen as 0 and filling out +1 to all neighbors.
This is essentially the same as a BFS explore, but... using the map as our "visited" we get a nice benefit
of being able to visually see the oxygen spread after
'''
from ComputerV4 import Computer, OutputInterrupt, InputInterrupt
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from copy import copy

WALL = 0
EMPTY = 1
WALKABLE = -1
OXYGEN = 2

DIRECTION = [1, 4, 2, 3]
TURNS = [-1j, 1, 1j, -1]


def get_tile(droid: Computer, param: int) -> int:
    try:
        droid.run()
    except InputInterrupt:
        droid.inputs.append(param)

    try:
        droid.run()
    except OutputInterrupt:
        return droid.outputs.pop()


def print_map(map):
    minx, maxx = min(int(pos.real) for pos in map), max(int(pos.real) for pos in map)
    miny, maxy = min(int(pos.imag) for pos in map), max(int(pos.imag) for pos in map)
    xoff, yoff = abs(minx), abs(miny)

    image = np.zeros((maxy - miny + 1, maxx - minx + 1))
    for pos, tile in map.items():
        x, y = int(pos.real) + xoff, int(pos.imag) + yoff
        image[y][x] = tile

    plt.imshow(image)
    plt.show()


def build_map(code):
    droid = Computer(code)

    origin, position = 0, 0
    map = {}
    fully_explored = False
    oxygen = 0
    dir_i = 0

    while not fully_explored:
        new_position = position + TURNS[dir_i]

        if new_position == origin:
            fully_explored = True

        tile = get_tile(droid, DIRECTION[dir_i])

        if tile == WALL:
            # turn right
            dir_i = (dir_i + 1) % 4
            map[new_position] = WALL
        elif tile == EMPTY or tile == OXYGEN:
            map[new_position] = tile
            if tile == OXYGEN:
                oxygen = new_position
            # move forward and turn left
            position = new_position
            dir_i = (dir_i - 1) % 4

    return map, oxygen


def shortest_path_to_oxygen(map):
    # starting at position (0, 0)
    todo = deque([(0, 1)])
    visited = set()

    while todo:
        current_pos, distance = todo.popleft()
        visited.add(current_pos)

        for neighbor in [current_pos + dir for dir in TURNS]:
            if neighbor in map and neighbor not in visited:
                if map[neighbor] == OXYGEN:
                    return distance
                if map[neighbor] == EMPTY:
                    todo.append((neighbor, distance + 1))


def oxygenate_world(map, oxygen):
    oxygenated_map = copy(map)
    todo = deque([(oxygen, 0)])
    minutes = 0

    while todo:
        pos, minutes = todo.popleft()
        oxygenated_map[pos] = minutes
        for neighbor in [pos + d for d in [-1j, 1, 1j, -1]]:
            if oxygenated_map[neighbor] == EMPTY:
                todo.append((neighbor, minutes + 1))

    return oxygenated_map, minutes


code = open('graph/inputs/2019-15.txt').read().strip()
map, oxygen = build_map(code)
print_map(map)

print("Part 1:", shortest_path_to_oxygen(map))

oxygenated_map, minutes = oxygenate_world(map, oxygen)
print("Part 2:", minutes)
print_map(oxygenated_map)
