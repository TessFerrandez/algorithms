'''
Given an array a[] of size n, and a number of queries q[[left, right]]
print the number of distinct integers in the subarray left to right

All a[i] <= 10 ** 6

ex:
a = [1, 1, 2, 1, 3]
q = [[0, 4], [1, 3], [2, 4]]

output: 3, 2, 3

# IDEA: Use Binary Indexed Tree
# 1. last_visit[i] holds right most index of number i in array a
# 2. Sort all queries in ascending order of their right end r
# 3. Create a binary indexed tree in an array bit[]
# - start traversing the array a and queries simultaneously and
#   check if last_visit[a[i]] is -1 or not, if not, update the bit array
#   with value -1 and the idx last_visit[a[i]]
# 4. Set last_visit[a[i]] = i and update the bit array with value 1 at idx i
# 5. Answer all queries whose value of r is equal to i by querying the bit array
#    this can be easily done with the queries sorted
# '''
from collections import defaultdict


def answer_queries(a, queries):
    queries.sort(key=lambda x: x[1])
    n = len(a)
    q = len(queries)

    bit = [0] * (n + 1)
    last_visit = defaultdict(lambda: -1)
    answer = [0] * q

    def update(idx, val):
        while idx <= n:
            bit[idx] += val
            idx += idx & -idx

    def query(idx):
        summ = 0
        while idx:
            summ += bit[idx]
            idx -= idx & -idx
        return summ

    query_counter = 0
    for i in range(n):
        if last_visit[a[i]] != -1:
            update(last_visit[a[i]] + 1, -1)
        last_visit[a[i]] = i
        update(i + 1, 1)

        while query_counter < q and queries[query_counter][1] == i:
            left, right, idx = queries[query_counter]
            answer[idx] = query(right + 1) - query(left)
            query_counter += 1

    return answer


assert answer_queries([1, 1, 2, 1, 3], [(0, 4, 0), (1, 3, 1), (2, 4, 2)]) == [3, 2, 3]
