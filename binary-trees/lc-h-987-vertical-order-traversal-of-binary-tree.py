from collections import defaultdict, deque
from typing import List, Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)

        todo = deque([(0, 0, root)])

        while todo:
            col, row, node = todo.popleft()
            columns[col].append((row, node.val))

            if node.left:
                todo.append((col - 1, row + 1, node.left))
            if node.right:
                todo.append((col + 1, row + 1, node.right))

        result = []
        for col in sorted(columns.keys()):
            sorted_col = sorted(columns[col])
            result.append([])
            for row, val in sorted_col:
                result[-1].append(val)

        return result


solution = Solution()
assert solution.verticalTraversal(deserialize([3,1,4,0,2,2])) == [[0],[1],[3,2,2],[4]]
assert solution.verticalTraversal(deserialize([3,9,20,None,None,15,7])) == [[9],[3,15],[20],[7]]
assert solution.verticalTraversal(deserialize([1,2,3,4,5,6,7])) == [[4],[2],[1,5,6],[3],[7]]
assert solution.verticalTraversal(deserialize([1,2,3,4,6,5,7])) == [[4],[2],[1,5,6],[3],[7]]
