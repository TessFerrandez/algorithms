from typing import List
from UnionFind import UnionFind


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        nodes = set()
        for equation in equations:
            nodes.add(equation[0])
            nodes.add(equation[3])

        uf = UnionFind(nodes)
        for equation in equations:
            if equation[1] == "=":
                uf.union(equation[0], equation[3])

        for equation in equations:
            if equation[1] == "!":
                if uf.find(equation[0]) == uf.find(equation[3]):
                    return False

        return True


solution = Solution()
assert not solution.equationsPossible(["a==b","b!=a"])
assert solution.equationsPossible(["b==a","a==b"])
