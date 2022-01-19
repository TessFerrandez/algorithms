'''
Given a 4x4 maze with doors
Get yourself from S (start) to V (vault)
# = fixed walls
|- = doors

To find out if the doors are opened or closed take MD5(hash + path so far (ex. DURR)) and get the hexdigest
First 4 chars are UDLR - b-f means OPEN and 0-a means closed

#########
#S| | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | |V#
#########

Assumption: We have no circular paths

Part 1: Shortest Path
---------------------
Algorithm:  BFS shortest path,
            No visited state as no cycles

Part 2: Longest Path
---------------------
Algorithm:  Recursive DFS to get all path lengths,
            Record the path length when dest is found
            longest path = max(all path lengths)
'''
from collections import deque
from typing import Set, Tuple, Dict, List, Deque
import hashlib


OPEN = 0
CLOSED = 1
SIZE = 4

def get_doors(path, hash):
    md5_result = hashlib.md5((hash + path).encode()).hexdigest()[:4]
    doors = [OPEN if "b" <= ch <= "f" else CLOSED for ch in md5_result]
    return doors


def get_neighbors(current, path, hash):
    neighbors = []
    doors = get_doors(path, hash)
    x, y = current
    # UP
    if y > 0 and doors[0] == OPEN:
        neighbors.append(((x, y - 1), "U"))
    # DOWN
    if y < SIZE - 1 and doors[1] == OPEN:
        neighbors.append(((x, y + 1), "D"))
    # LEFT
    if x > 0 and doors[2] == OPEN:
        neighbors.append(((x - 1, y), "L"))
    # RIGHT
    if x < SIZE - 1 and doors[3] == OPEN:
        neighbors.append(((x + 1, y), "R"))
    return neighbors


def shortest_path(source, dest, hash) -> str:
    todo = deque([(source, "")])

    if source == dest:
        return ""

    while todo:
        current, path = todo.popleft()

        for neighbor, direction in get_neighbors(current, path, hash):
            if neighbor == dest:
                return path + direction

            todo.append((neighbor, path + direction))

    return ""


def get_all_path_lenghts(source, dest, hash, path_lengths, path='', direction=''):
    '''
    recursive depth first search (without visited, as we can visit the same room several times)
    assumes acyclic graphs (no circular paths - so we don't walk around in endless loops)
    '''
    path += direction

    if source == dest:
        path_lengths.append(len(path))
    else:
        for neighbor, direction in get_neighbors(source, path, hash):
            get_all_path_lenghts(neighbor, dest, hash, path_lengths, path, direction)

    path = path[:-1]


def longest_path(source, dest, hash) -> int:
    ''' assumes acyclic graphs '''
    path_lengths = []
    get_all_path_lenghts(source, dest, hash, path_lengths)
    return max(path_lengths)


print("Part 1:", shortest_path((0, 0), (3, 3), "lpvhkcbi"))
print("Part 2:", longest_path((0,0), (3, 3), "lpvhkcbi"))
