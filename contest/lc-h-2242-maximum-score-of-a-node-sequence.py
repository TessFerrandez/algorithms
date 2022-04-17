from bisect import insort_left
from collections import defaultdict
from typing import List


class Solution:
    # my solution - doesnt find all solutions
    def maximumScore1(self, scores: List[int], edges: List[List[int]]) -> int:
        def get_all_simple_paths(graph, source, dest):
            paths = []

            def dfs(graph, source, dest, visited, path):
                visited.add(source)
                path.append(source)

                if len(path) > 5:
                    return []
                if source == dest and len(path) == 4:
                    paths.append(path.copy())
                else:
                    for neighbor in graph[source]:
                        if neighbor not in visited:
                            dfs(graph, neighbor, dest, visited, path)

                path.pop()
                visited.remove(source)

            dfs(graph, source, dest, set(), [])
            return paths

        graph = defaultdict(list)
        for f, t in edges:
            graph[f].append(t)
            graph[t].append(f)

        n = len(scores)
        max_score = -1
        for i in range(n):
            for j in range(n):
                if i != j:
                    for path in get_all_simple_paths(graph, i, j):
                        print(path)
                        score = 0
                        for node in path:
                            score += scores[node]
                        max_score = max(score, max_score)

        return max_score

    # solution from Bakerston
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        '''
        focus on a-b in a chain X-a-b-Y
        for all pairs a-b (that we find in edges) - find the neighbor X with the highest score and Y with the highest score
        the maximum score with a-b is X + a + b + Y
        '''
        # store top 3 neighbors of a node
        top3 = defaultdict(list)

        def func(a, b, e):
            insort_left(top3[a], [e, b])
            if len(top3[a]) > 3:
                top3[a].pop(0)

        # update the info of top 3 neighbors of each node
        for a, b in edges:
            func(a, b, scores[b])
            func(b, a, scores[a])

        answer = -1
        for a, b in edges:
            # if there is less than 2 neighbors of a node, skip this pair
            if len(top3[a]) < 2 or len(top3[b]) < 2:
                continue
            for c in top3[a]:
                for d in top3[b]:
                    # find the max score of two non-duplicate neighbors of a and b
                    if c[1] not in [a, b] and d[1] not in [a, b] and c[1] != d[1]:
                        answer = max(answer, scores[a] + scores[b] + c[0] + d[0])
        return answer


solution = Solution()
assert solution.maximumScore([18,6,4,9,8,2], [[0,1],[0,2],[0,3],[0,4],[0,5],[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]) == 41
assert solution.maximumScore([14,12,10,8,1,2,3,1], [[1,0],[2,0],[3,0],[4,0],[5,1],[6,1],[7,1],[2,1]]) == 44
assert solution.maximumScore([16,21,22,2,24,21,12,17,2,24], [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,0]]) == 83
assert solution.maximumScore([5,2,9,8,4], [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]) == 24
assert solution.maximumScore([9,20,6,4,11,12], [[0,3],[5,3],[2,4],[1,3]]) == -1
