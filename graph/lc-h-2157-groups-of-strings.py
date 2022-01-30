'''
You are given a 0-indexed array of strings words. Each string consists of lowercase English letters only. No letter occurs more than once in any string of words.

Two strings s1 and s2 are said to be connected if the set of letters of s2 can be obtained from the set of letters of s1 by any one of the following operations:

Adding exactly one letter to the set of the letters of s1.
Deleting exactly one letter from the set of the letters of s1.
Replacing exactly one letter from the set of the letters of s1 with any letter, including itself.
The array words can be divided into one or more non-intersecting groups. A string belongs to a group if any one of the following is true:

It is connected to at least one other string of the group.
It is the only string present in the group.
Note that the strings in words should be grouped in such a manner that a string belonging to a group cannot be connected to a string present in any other group. It can be proved that such an arrangement is always unique.

Return an array ans of size 2 where:

ans[0] is the total number of groups words can be divided into, and
ans[1] is the size of the largest group
'''
from typing import List
from collections import defaultdict, deque, Counter


class Solution:
    # my solution -- time limit exceeded
    def groupStrings1(self, words: List[str]) -> List[int]:
        def get_bits(word):
            bits = ['0'] * 26
            for ch in word:
                bits[ord(ch) - 97] = '1'
            return int(''.join(bits), 2)

        def is_connected(word1, word2):
            if len(word1) == len(word2):
                ones = bin(get_bits(word1) ^ get_bits(word2)).count('1')
                if ones == 2 or ones == 0:
                    return True
            elif abs(len(word1) - abs(len(word2))) == 1:
                ones = bin(get_bits(word1) ^ get_bits(word2)).count('1')
                if ones == 1:
                    return True
            return False

        def build_graph(words):
            graph = defaultdict(list)

            for i in range(len(words)):
                graph[i].append(i)
                for j in range(1, len(words)):
                    if i != j and is_connected(words[i], words[j]):
                        graph[i].append(j)
                        graph[j].append(i)

            return graph

        def word_in_groups(word, groups):
            for group in groups:
                if word in group:
                    return True
            return False

        def get_reacheable(graph, key):
            visited = set()
            todo = deque([key])

            while todo:
                current = todo.popleft()

                if current in visited:
                    continue

                visited.add(current)

                for neighbor in graph[current]:
                    todo.append(neighbor)

            return visited

        def find_groups(graph):
            groups = []

            for word in graph:
                if word_in_groups(word, groups):
                    continue
                groups.append(get_reacheable(graph, word))

            return [len(groups), max(len(group) for group in groups)]

        graph = build_graph(words)
        return find_groups(graph)

    # from solutions - bitmask + union find - time limit exceeded
    def groupStrings2(self, words: List[str]) -> List[int]:
        n = len(words)
        graph = {}
        groups = []

        def find(x):
            if x != groups[x]:
                groups[x] = find(groups[x])
            return groups[x]

        def connected(word):
            for i in range(26):
                yield word ^ (1 << i)
                if (word & (1 << i)) > 0:
                    for j in range(26):
                        if word & (1 << j) == 0:
                            yield word ^ (1 << i) ^ (1 << j)

        for i, word in enumerate(words):
            word_bitmask = sum(1 << (ord(char) - ord('a')) for char in word)
            groups.append(graph.setdefault(word_bitmask, i))
            for word2 in connected(word_bitmask):
                if word2 in graph:
                    i, j = find(graph[word_bitmask]), find(graph[word2])
                    if i != j:
                        groups[i] = j

        count = Counter(find(i) for i in range(n))
        return [len(count), max(count.values())]

    # from discuss solutions
    def groupStrings(self, words: List[str]) -> List[int]:
        masks = {sum(1 << (ord(i) - ord("a")) for i in word): j for j, word in enumerate(words)}

        graph = defaultdict(list)
        masks = defaultdict(list)

        for i, word in enumerate(words):
            chars = [ord(ch) - ord("a") for ch in word]
            mask = sum(1 << ch for ch in chars)
            for ch in chars:
                masks[mask - (1 << ch) + (1 << 26)].append(i)
                if mask - (1 << ch) not in masks:
                    continue
                i2 = masks[mask - (1 << ch)]
                graph[i] += [i2]
                graph[i2] += [i]

        for x in masks.values():
            for a, b in zip(x, x[1:]):
                graph[a] += [b]
                graph[b] += [a]

        visited, n_groups, max_group_size = set(), 0, 0
        for node in range(len(words)):
            if node in visited:
                continue

            group_size, todo = 1, [node]
            visited.add(node)

            while todo:
                node = todo.pop()
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    group_size += 1
                    visited.add(neighbor)
                    todo += [neighbor]

            max_group_size = max(max_group_size, group_size)
            n_groups += 1

        return [n_groups, max_group_size]


solution = Solution()
assert solution.groupStrings(['a', 'b', 'ab', 'cde']) == [2, 3]
assert solution.groupStrings(['a', 'ab', 'abc']) == [1, 3]
