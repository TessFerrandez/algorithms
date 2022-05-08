def knapsack1(weights, values, capacity):
    def best_combo(capacity, n):
        if n == 0 or capacity == 0:
            return 0

        # weight of nth item is more than the
        # knapsack capacity so we can't include it
        if weights[n - 1] > capacity:
            return best_combo(capacity, n - 1)

        # return the maximum of
        # a) nth item included
        # b) nth item not included
        else:
            return max(
                values[n - 1] + best_combo(capacity - weights[n - 1], n - 1),
                best_combo(capacity, n - 1)
            )

    return best_combo(capacity, len(values))


def knapsack(weights, values, capacity):
    n = len(values)
    sack = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for cap_left in range(capacity + 1):
            if i == 0 or cap_left == 0:
                sack[i][cap_left] = 0
            elif weights[i - 1] <= cap_left:
                sack[i][cap_left] = max(
                    values[i - 1] + sack[i - 1][cap_left - weights[i - 1]],
                    sack[i - 1][cap_left])
            else:
                sack[i][cap_left] = sack[i - 1][cap_left]

    return sack[n][capacity]


assert knapsack([10, 20, 30], [60, 100, 120], 50) == 220
