from collections import deque
from TreeNode import TreeNode
from copy import deepcopy


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not cloned:
            return None

        todo = deque()
        todo.append(cloned)

        while todo:
            node = todo.popleft()
            if node.val == target.val:
                return node
            if node.left:
                todo.append(node.left)
            if node.right:
                todo.append(node.right)

        return None


solution = Solution()
node = TreeNode(3, TreeNode(6), TreeNode(19))
tree = TreeNode(7, TreeNode(4), node)
cloned = deepcopy(tree)
assert solution.getTargetCopy(tree, cloned, node).val == 3
