from collections import deque


def get_neighbors(graph, current):
    # return the neighbors
    return graph[current]


# Breadth First Search (BFS) based shortest path
def shortest_path(graph, start, target):
    todo = deque([start])
    previous = {start: None}        # replaces seen from BFS

    while todo:
        current = todo.popleft()    # fifo
        if current == target:
            break

        for neighbor in get_neighbors(graph, current):
            if neighbor not in previous:
                previous[neighbor] = current
                todo.append(neighbor)

    # no target found
    if target not in previous:
        return []

    # backtrack from current
    path = []
    current = target

    while current:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path


graph = {1: [2, 3],
         2: [3, 4],
         3: [5],
         4: [5],
         5: None}

print(shortest_path(graph, 1, 5))
