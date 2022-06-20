from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    # dynamic programming
    def minCameraCover1(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            '''
            solve returns a tuple (0, 1, 2)
            0 : Strict ST - all nodes below this are covered but not this one
            1 : Normal ST - all nodes below and incl this are covered - no camera
            2 : Placed Camera - all nodes below this are covered + camera here

            to calculate 0, 1, 2
            0 : To cover strict, children need to be 1
            1 : To cover normal, children need to be 1 or 2, at least one needs to be 2
            2 : To cover cam, children can be any state, and cam of course adds one cam
            '''

            if not node:
                return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(solve(root)[1:])

    # greedy
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        '''
        place cameras from the bottom up
        if a nodes children are covered and it has a parent
        then it is strictly better to place the camera at the nodes parent
        '''
        self.camerasNeeded = 0

        covered = {None}

        def dfs(node, parent=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if not parent and node not in covered or node.left not in covered or node.right not in covered:
                    self.camerasNeeded += 1
                    covered.update({node, parent, node.left, node.right})

        dfs(root)
        return self.camerasNeeded


solution = Solution()
tree = deserialize([0, 0, None, 0, 0])
assert solution.minCameraCover(tree) == 1

tree = deserialize([0, 0, None, 0, None, 0, None, None, 0])
assert solution.minCameraCover(tree) == 2
