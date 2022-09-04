'''
A group of friends went on holiday and sometimes lent each other money.
For example, Alice paid for Bill's lunch for $10.
Then later Chris gave Alice $5 for a taxi ride.

We can model each transaction as a tuple (x, y, z) which means
person x gave person y $z.

Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively
(0, 1, 2 are the person's ID), the transactions can be represented as
[[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people,
return the minimum number of transactions required to settle the debt.

Note: A transaction will be given as a tuple (x, y, z).
Note that x ≠ y and z > 0. Person's IDs may not be linear,
e.g. we could have the persons 0, 1, 2 or we could also have the persons
0, 2, 6.
'''
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minTransfers(self, transactions: List[int]) -> List[int]:
        def make_transactions():
            net_result = defaultdict(int)
            for fr, to, value in transactions:
                net_result[fr] -= value
                net_result[to] += value

            return list(net_result.values())

        def process(debts, start):
            min_transactions = inf

            while start < len(debts) and debts[start] == 0:
                start += 1

            for i in range(start + 1, len(debts)):
                if debts[i] == 0:
                    continue
                if (debts[start] > 0 and debts[i] < 0) or (debts[start] < 0 and debts[i] > 0):
                    debts[i] += debts[start]
                    min_transactions = min(min_transactions, process(debts, start + 1) + 1)
                    debts[i] -= debts[start]

            if min_transactions != inf:
                return min_transactions

            return 0

        debts = make_transactions()
        return process(debts, 0)


solution = Solution()
assert solution.minTransfers([[0,1,10], [2,0,5]]) == 2
assert solution.minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]]) == 1
