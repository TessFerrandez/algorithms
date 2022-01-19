'''
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

ALGO -- in parenthesis - (W) opponent wins (L) opponent looses
-----------
Stones  Pick1   Pick2   Pick3   W/L
1       0(L)                    W
2       1(W)    0               W
3       2(W)    1(W)    0(L)    W
4       3(W)    2(W)    1(W)    L
5       4(L)    3(W)    2(W)    W
6       5(W)    4(L)    3(W)    W
7       6(W)    5(W)    4(L)    W
8       7(W)    6(W)    5(W)    L
...
We loose if stones % 4 == 0
'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


solution = Solution()
assert solution.canWinNim(1) == True
assert solution.canWinNim(2) == True
assert solution.canWinNim(4) == False
