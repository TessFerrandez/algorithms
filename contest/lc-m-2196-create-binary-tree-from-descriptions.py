from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        has_parent = {}

        for val, child, isleft in descriptions:
            if val in node_map:
                node = node_map[val]
            else:
                node = TreeNode(val)
                node_map[val] = node
                has_parent[val] = False

            if child in node_map:
                child_node = node_map[child]
            else:
                child_node = TreeNode(child)
                node_map[child] = child_node

            has_parent[child] = True

            if isleft == 1:
                node.left = child_node
            else:
                node.right = child_node

        for node in has_parent:
            if not has_parent[node]:
                return node_map[node]


solution = Solution()
result = solution.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
result = solution.createBinaryTree([[1,2,1],[2,3,0],[3,4,1]])
