'''
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
'''
from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def onediff(word1, word2):
            diff = 0
            for i in range(8):
                if word1[i] != word2[i]:
                    if diff == 1:
                        return False
                    diff = 1
            return True

        bank = set(bank)
        todo = deque([(0, start)])

        if start in bank:
            bank.remove(start)

        while todo:
            steps, mutation = todo.popleft()
            if mutation == end:
                return steps

            neighbors = set()
            for gene_string in bank:
                if onediff(gene_string, mutation):
                    neighbors.add(gene_string)
                    todo.append((steps + 1, gene_string))
            for neighbor in neighbors:
                bank.remove(neighbor)

        return -1


solution = Solution()
assert solution.minMutation('AACCGGTT', 'AACCGGTA', ["AACCGGTA"]) == 1
assert solution.minMutation('AACCGGTT', 'AAACGGTA', ["AACCGGTA","AACCGCTA","AAACGGTA"]) == 2
assert solution.minMutation('AAAAACCC', 'AACCCCCC', ["AAAACCCC","AAACCCCC","AACCCCCC"]) == 3
