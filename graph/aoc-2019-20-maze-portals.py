# based on
# https://github.com/matnad/aoc19/blob/master/day20/day20a.py
'''
Given a maze:

         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       

the . next to AA is the start point
the . next to ZZ is the end point
the . next to BC is a portal, that automatically transports us to
      the other BC portal (taking one step)

Part 1: What is the shortest path from AA - ZZ if you can use portals?
----------------------
Algorithm:
    Same as for usual mazes, but now the other BC is a neighbor of the first BC
    For the solution below, we use the networkx library, but we could have also
    just implemented this as a BFS - with the addition that BC1-BC2 are neighbors

Part 2: The maze is multi story/level
----------------------
   AA and ZZ are only available on level 0, but if you enter an inner portal
   (in the inner yard) to transport to an outer portal you go up one level.
   Similarily, if you go through an outer portal and transport to an inner portal,
   you go down one level.

Algorithm:
    We can duplicate the graph a number of times (one per level) - and connect the inner
    portals to the outer portals of the next level (like an escalator). and likewise a
    downward escalator for outer to inner.

    The number of levels we need, will always be at maximum the same as the number of portals.

    With this new map, we can just do a networkx search (djikstra) or a BFS search for the
    shortest path from start, level 0 to end, level 0
'''

from collections import defaultdict
from string import ascii_uppercase
import networkx as nx
from networkx.classes import graph
from networkx.classes.function import neighbors


def get_neighbors(point):
    return [(point[0] + dx, point[1] + dy) for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]]


def get_portals(grid):
    start = end = None
    portals = defaultdict(list)

    for pos, ch in grid.items():
        if ch in ascii_uppercase:
            neighbors = [neighbor for neighbor in get_neighbors(pos) if neighbor in grid]
            if len(neighbors) == 2:
                # letter and path_way
                if grid[neighbors[0]] in ascii_uppercase:
                    letter, path_way = neighbors
                else:
                    path_way, letter = neighbors
                portal = ''.join(sorted(ch + grid[letter]))
                portals[portal].append(path_way)

                if portal == 'AA':
                    start = path_way
                elif portal == 'ZZ':
                    end = path_way

    return portals, start, end


def parse_raw(raw_maze):
    rows = raw_maze.splitlines()
    maze = {}
    width, height = len(rows[0]), len(rows)

    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch != ' ' and ch != '#':
                maze[(x, y)] = ch

    portals, start, end = get_portals(maze)

    return maze, width, height, portals, start, end


def build_graph(maze, portals):
    maze_graph = nx.Graph()

    # connect all path ways
    for pos, ch in maze.items():
        if ch == '.':
            maze_graph.add_node(pos)
            neighbors = get_neighbors(pos)
            for neighbor in neighbors:
                if neighbor in maze and maze[neighbor] == '.':
                    maze_graph.add_edge(pos, neighbor)

    # connect the portals
    for positions in portals.values():
        if len(positions) == 2:
            maze_graph.add_edge(positions[0], positions[1])

    return maze_graph


def build_level_graph(maze, portals):
    maze_graph = nx.Graph()
    levels = len(portals)       # max recursion depth

    # connect all path ways
    for pos, ch in maze.items():
        if ch == '.':
            for i in range(levels):
                # create the node on each level
                maze_graph.add_node((*pos, i))
            neighbors = get_neighbors(pos)
            for neighbor in neighbors:
                if neighbor in maze and maze[neighbor] == '.':
                    for i in range(levels):
                        # connect to the path way on each level
                        maze_graph.add_edge((*pos, i), (*neighbor, i))

    # connect the portals
    for positions in portals.values():
        if len(positions) == 2:
            # check which portal is outer and which is inner
            if positions[0][0] in [2, width - 3] or positions[0][1] in [2, height - 3]:
                outer, inner = positions
            else:
                inner, outer = positions

            for i in range(levels - 1):
                # inner portals lead to outer portals on the next level
                # outer portals lead to inner portals on the prev level
                maze_graph.add_edge((*inner, i), (*outer, i + 1))
                maze_graph.add_edge((*outer, i + 1), (*inner, i))

    return maze_graph


raw_maze = '''         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       
'''

raw_maze = open('graph/inputs/2019-20.txt').read()

maze, width, height, portals, start, end = parse_raw(raw_maze)
maze_graph = build_graph(maze, portals)
print("Part 1:", nx.shortest_path_length(maze_graph, start, end))

maze_graph = build_level_graph(maze, portals)
print("Part 2:", nx.shortest_path_length(maze_graph, (*start, 0), (*end, 0)))
