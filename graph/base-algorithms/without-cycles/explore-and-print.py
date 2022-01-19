from collections import deque

def breadth_first_explore_and_print(graph, start):
    todo = deque([start])

    while todo:
        current = todo.popleft()
        print(current, end=" ")
        for neighbor in graph[current]:
            todo.append(neighbor)

    print()


def depth_first_explore_and_print(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current, end=' ')
        for neighbor in graph[current]:
            stack.append(neighbor)

    print()


def depth_first_recursive_explore_and_print(graph, source):
    print(source, end=' ')
    for neighbor in graph[source]:
        depth_first_recursive_explore_and_print(graph, neighbor)


graph = {'a': ['b', 'c'],
         'b': ['d'],
         'c': ['e'],
         'd': ['f'],
         'e': [],
         'f': []}


breadth_first_explore_and_print(graph, 'a')
depth_first_explore_and_print(graph, 'a')
depth_first_recursive_explore_and_print(graph, 'a')
