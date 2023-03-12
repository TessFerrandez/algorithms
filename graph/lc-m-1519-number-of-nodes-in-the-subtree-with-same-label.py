from collections import defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        dupes = [0 for _ in range(n)]

        def dfs(node, parent):
            if node not in graph:
                return {labels[node]: 1}

            temp = defaultdict(int)
            for child in graph[node]:
                if child != parent:
                    dct = dfs(child, node)
                    for k in dct:
                        temp[k] += dct[k]

            dupes[node] = temp[labels[node]] + 1
            temp[labels[node]] += 1
            return temp

        dfs(0, -1)
        for i in range(len(dupes)):
            if dupes[i] == 0:
                dupes[i] = 1

        return dupes


solution = Solution()
assert solution.countSubTrees(n=7, edges=[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels="abaedcd") == [2,1,1,1,1,1,1]
assert solution.countSubTrees(n=4, edges=[[0,1],[1,2],[0,3]], labels="bbbb") == [4, 2, 1, 1]
assert solution.countSubTrees(n=5, edges=[[0,1],[0,2],[1,3],[0,4]], labels="aabab") == [3, 2, 1, 1, 1]
