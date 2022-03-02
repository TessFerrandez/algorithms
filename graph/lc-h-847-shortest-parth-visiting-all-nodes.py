'''
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
'''
class Solution:
    def shortestPathLength_dp(self, graph):
        def dp(node, mask):
            state = (node, mask)
            if state in cache:
                return cache[state]
            if mask & (mask - 1) == 0:
                # Base case - mask only has a single "1", which means
                # that only one node has been visited (the current node)
                return 0

            cache[state] = float("inf")     # Avoid infinite loop in recursion
            for neighbor in graph[node]:
                if mask & (1 << neighbor):
                    already_visited = 1 + dp(neighbor, mask)
                    not_visited = 1 + dp(neighbor, mask ^ (1 << node))
                    cache[state] = min(cache[state], already_visited, not_visited)

            return cache[state]

        n = len(graph)
        ending_mask = (1 << n) - 1
        cache = {}

        return min(dp(node, ending_mask) for node in range(n))

    def shortestPathLength(self, graph):
        if len(graph) == 1:
            return 0

        n = len(graph)
        ending_mask = (1 << n) - 1
        queue = [(node, 1 << node) for node in range(n)]
        seen = set(queue)

        steps = 0
        while queue:
            next_queue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    if next_mask == ending_mask:
                        return 1 + steps

                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        next_queue.append((neighbor, next_mask))

            steps += 1
            queue = next_queue


solution = Solution()
assert solution.shortestPathLength([[1, 2, 3], [0], [0], [0]]) == 4
assert solution.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]) == 4
