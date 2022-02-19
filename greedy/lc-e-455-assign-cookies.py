'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
'''
from typing import List


class Solution:
    def findContentChildren(self, children: List[int], cookies: List[int]) -> int:
        children.sort()
        cookies.sort()

        content = 0
        cookie_i, child_i = 0, 0
        while cookie_i < len(cookies) and child_i < len(children):
            while cookie_i < len(cookies) and cookies[cookie_i] < children[child_i]:
                cookie_i += 1

            if cookie_i < len(cookies):
                content += 1
                cookie_i += 1
                child_i += 1
            else:
                break

        return content


solution = Solution()
assert solution.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]) == 2
assert solution.findContentChildren([1, 2, 3], [1, 1]) == 1
assert solution.findContentChildren([1, 2], [1, 2, 3])
assert solution.findContentChildren([1, 2], []) == 0
