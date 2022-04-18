from bisect import insort_right
from collections import defaultdict, deque
from typing import List


class Solution:
    # my solution - TLE
    def longestPath1(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)

        for i, p in enumerate(parent):
            if p != -1:
                if s[i] != s[p]:
                    graph[p].append(i)
                    graph[i].append(p)

        def get_longest_path(node):
            visited = set()
            max_len = 0
            todo = deque([(node, 1)])
            while todo:
                n, plen = todo.popleft()
                max_len = max(max_len, plen)
                visited.add(n)
                for neighbor in graph[n]:
                    if neighbor not in visited:
                        todo.append((neighbor, plen + 1))

            return max_len

        longest_path = 1
        for node in graph:
            l_path = get_longest_path(node)
            longest_path = max(longest_path, l_path)

        return longest_path

    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        child_num = [0] * n

        # count the number of children for each node
        for a in parent[1:]:
            child_num[a] += 1

        # longest valid chain with node i as parent
        longest = [[0] for _ in range(n)]

        # add all leaf nodes to deque
        todo = deque()
        for i in range(n):
            if child_num[i] == 0:
                todo.append([i, 1])

        answer = 1
        while todo:
            curr_i, curr_l = todo.popleft()
            curr_p = parent[curr_i]

            # minus the number of unvisited child node by 1
            child_num[curr_p] -= 1

            # if the child has different char with parent
            if s[curr_p] != s[curr_i]:
                insort_right(longest[curr_p], curr_l)
                if len(longest[curr_p]) > 2:
                    longest[curr_p].pop(0)

            # if the parent has 0 unvisited children
            # add it to deque
            if child_num[curr_p] == 0:
                answer = max(answer, 1 + sum(longest[curr_p][-2:]))
                todo.append([curr_p, 1 + longest[curr_p][-1]])

        return answer


solution = Solution()
assert solution.longestPath([-1], "z") == 1
assert solution.longestPath([-1,0,0,1,1,2], "abacbe") == 3
assert solution.longestPath([-1,0,0,0], "aabc") == 3
