from collections import defaultdict
from typing import List


class Solution:
    # union find
    def possibleBipartition2(self, n: int, dislikes: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if rank[x] <= rank[y]:
                parent[x] = y
            else:
                parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

        last_dislike = [-1] * n

        for a, b in dislikes:
            a -= 1
            b -= 1

            if find(a) == find(b):
                # both hate the same person
                return False
            else:
                if last_dislike[a] >= 0:
                    # put people who dislike a together
                    union(last_dislike[a], b)
                if last_dislike[b] >= 0:
                    # put people who dislike b together
                    union(last_dislike[b], a)
                last_dislike[a] = b
                last_dislike[b] = a

        return True

    # dfs
    def possibleBipartition1(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        plt = defaultdict(int)

        for a, b in dislikes:
            graph[a].add(b)
            graph[b].add(a)

        def dfs(node, color) -> bool:
            plt[node] = color
            for i in graph[node]:
                if plt[i] == color:
                    return False
                if plt[i] == 0 and not dfs(i, -color):
                    return False
            return True

        for i in range(1, n + 1):
            if plt[i] == 0 and not dfs(i, 1):
                return False

        return True

    # dfs explanation
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        NO_GROUP, GROUP1 = 0, 1     # GROUP2 = -1

        # dfs
        def try_assign(person, group):
            # assign person to group
            group_assignment[person] = group

            for enemy in dislike_graph[person]:
                # enemy is assigned to persons group - fail
                if group_assignment[enemy] == group:
                    return False

                # try assigning the enemy to the other group (-group)
                if group_assignment[enemy] == NO_GROUP and not try_assign(enemy, -group):
                    return False

            return True

        if n == 1 or not dislikes:
            return True

        dislike_graph = defaultdict(set)
        group_assignment = defaultdict(int)

        for person, enemy in dislikes:
            dislike_graph[person].add(enemy)
            dislike_graph[enemy].add(person)

        for person in range(1, n + 1):
            if group_assignment[person] == NO_GROUP and not try_assign(person, GROUP1):
                # we can't assign person an their enemies to different groups
                return False

        return True


solution = Solution()
assert solution.possibleBipartition(4, [[1,2],[1,3],[2,4]])
assert not solution.possibleBipartition(3, [[1,2],[1,3],[2,3]])
assert not solution.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]])
