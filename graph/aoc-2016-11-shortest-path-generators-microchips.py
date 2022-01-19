'''
F4 .  .  .  .  .
F3 .  .  .  LG .
F2 .  HG .  .  .
F1 E  .  HM .  LM

Generators and Microchips

Question:
    What is the minimum amount of steps to move all items to floor 4?

Rules:
    - Elevator will move with 1 or 2 items
    - Elevator always moves one step at a time
    - A chip will fry if other generators are on the same floor unless it's own generator is there

Strategy:
    Algorithm:              BFS Shortest Path
    State representation:   "01020" (for the state above)
    Neighbors:              All moves from current state (1 or 2 items up or down from elevator floor)
                            that result in a valid state
    Target state:           "33333" (all items on floor 4 (3 0-indexed))

Optimizations:
    Pairs are interchangeable, so 01120 == 02011 - we use this in visited
'''
from collections import deque
from itertools import combinations


def make_move(state, items_to_move, elevator_floor, dir):
    lst_state = list(state)
    new_elevator_floor = str(elevator_floor + dir)
    lst_state[0] = new_elevator_floor
    for pos in items_to_move:
        lst_state[pos] = new_elevator_floor
    return ''.join(lst_state)


def fries_chip(state):
    pairs = [state[x: x + 2] for x in range(1, len(state), 2)]
    generators = state[1::2]

    for generator, chip in pairs:
        if generator != chip:
            if chip in generators:
                return True

    return False


def get_next_states(state):
    new_states = []

    elevator_floor = state[0]
    floor_items = [i for i in range(1, len(state)) if state[i] == elevator_floor]
    options = [list(perm) for perm in combinations(floor_items, 2)] + [[item] for item in floor_items]

    for option in options:
        elevator_floor = int(elevator_floor)
        if elevator_floor > 0:
            new_state = make_move(state, option, elevator_floor, -1)
            if not fries_chip(new_state):
                new_states.append(new_state)
        if elevator_floor < 3:
            new_state = make_move(state, option, elevator_floor, 1)
            if not fries_chip(new_state):
                new_states.append(new_state)

    return new_states


def sort_state(state):
    pairs = [state[x: x + 2] for x in range(1, len(state), 2)]
    pairs.sort()
    return state[0] + ''.join(pairs)


def shortest_path(source, destination) -> int:
    todo = deque([(source, 0)])
    visited = set([sort_state(source)])

    if source == destination:
        return 0

    while todo:
        current, distance = todo.popleft()

        for new_state in get_next_states(current):
            if new_state == destination:
                return distance + 1

            if sort_state(new_state) not in visited:
                visited.add(sort_state(new_state))
                todo.append((new_state, distance + 1))

    return -1


# print(shortest_path("01020", "33333"))
print("Part 1:", shortest_path("00000121111", "33333333333"))
print("Part 2:", shortest_path("000001211110000", "333333333333333"))
