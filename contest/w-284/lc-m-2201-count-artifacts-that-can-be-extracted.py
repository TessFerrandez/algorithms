'''
There is an n x n 0-indexed grid with some artifacts buried in it. You are given the integer n and a 0-indexed 2D integer array artifacts describing the positions of the rectangular artifacts where artifacts[i] = [r1i, c1i, r2i, c2i] denotes that the ith artifact is buried in the subgrid where:

(r1i, c1i) is the coordinate of the top-left cell of the ith artifact and
(r2i, c2i) is the coordinate of the bottom-right cell of the ith artifact.
You will excavate some cells of the grid and remove all the mud from them. If the cell has a part of an artifact buried underneath, it will be uncovered. If all the parts of an artifact are uncovered, you can extract it.

Given a 0-indexed 2D integer array dig where dig[i] = [ri, ci] indicates that you will excavate the cell (ri, ci), return the number of artifacts that you can extract.

The test cases are generated such that:

No two artifacts overlap.
Each artifact only covers at most 4 cells.
The entries of dig are unique.
'''
from collections import defaultdict
from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        artifact_squares = defaultdict(list)
        squares = {}

        artifact = 0
        for r1, c1, r2, c2 in artifacts:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    artifact_squares[artifact].append((r, c))
                    squares[(r, c)] = artifact
            artifact += 1

        count = 0
        for r, c in dig:
            if (r, c) in squares:
                artifact = squares[(r, c)]
                artifact_squares[artifact].remove((r, c))
                if not artifact_squares[artifact]:
                    count += 1

        return count


solution = Solution()
assert solution.digArtifacts(5, [[3,1,4,1],[1,1,2,2],[1,0,2,0],[4,3,4,4],[0,3,1,4],[2,3,3,4]], [[0,0],[2,1],[2,0],[2,3],[4,3],[2,4],[4,1],[0,2],[4,0],[3,1],[1,2],[1,3],[3,2]]) == 1
assert solution.digArtifacts(2, [[0,0,0,0],[0,1,1,1]], [[0,0],[0,1]]) == 1
assert solution.digArtifacts(2, [[0,0,0,0],[0,1,1,1]], [[0,0],[0,1],[1,1]]) == 2
