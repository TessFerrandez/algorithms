from queue import PriorityQueue


# see contest/lc-h-2290... for better implementation with heap
def djikstra(graph, start):
    visited = set()
    previous = {node: None for node in graph}
    costs = {node: 10**9 for node in graph}
    costs[start] = 0

    todo = PriorityQueue()
    todo.put((0, start))

    while not todo.empty():
        current_cost, current = todo.get()
        visited.add(current)

        for neighbor in graph[current]:
            neighbor_cost = graph[current][neighbor]
            if neighbor not in visited:
                old_cost = costs[neighbor]
                new_cost = current_cost + neighbor_cost
                if new_cost < old_cost:
                    previous[neighbor] = current
                    todo.put((new_cost, neighbor))
                    costs[neighbor] = new_cost

    return costs, previous


graph = {
    'A': {'B': 1, 'D': 1},
    'B': {'A': 1, 'C': 6, 'E': 3},
    'C': {'B': 1, 'F': 8},
    'D': {'A': 1, 'E': 3, 'G': 2},
    'E': {'B': 1, 'D': 1, 'F': 8, 'H': 1},
    'F': {'C': 6, 'E': 3, 'I': 3},
    'G': {'D': 1, 'H': 1},
    'H': {'E': 3, 'G': 2, 'I': 3},
    'I': {'F': 8, 'H': 1}
}


costs, previous = djikstra(graph, 'A')
print(costs)
print(previous)
