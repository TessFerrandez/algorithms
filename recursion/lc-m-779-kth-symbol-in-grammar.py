'''
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
'''
from math import log2, floor


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def get_k(k):
            if k == 0:
                return 0

            n = floor(log2(k))
            return 1 - get_k(k % (2 ** n))

        return get_k(k - 1)


solution = Solution()
assert solution.kthGrammar(2, 2) == 1
assert solution.kthGrammar(5, 5) == 1
assert solution.kthGrammar(5, 8) == 1
assert solution.kthGrammar(5, 9) == 1
assert solution.kthGrammar(5, 16) == 0
assert solution.kthGrammar(20, 16) == 0
assert solution.kthGrammar(30, 423336352) == 0
