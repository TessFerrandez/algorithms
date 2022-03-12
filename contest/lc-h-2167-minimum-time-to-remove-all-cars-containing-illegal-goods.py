class Solution:
    # memory limit exceeded
    def minimumTime_mle(self, s: str) -> int:
        cache = {}

        def min_time(indices, start, end):
            if not indices:
                return 0

            if (indices, start, end) in cache:
                return cache[(indices, start, end)]

            remove_middle = 2 * len(indices)
            cost_left = 1 if indices[0] == start else indices[0] - start + 1
            remove_left = cost_left + min_time(indices[1:], indices[0] + 1, end)
            cost_right = 1 if indices[-1] == end else end - indices[-1] + 1
            remove_right = cost_right + min_time(indices[:-1], start, indices[-1] - 1)

            min_result = min(remove_middle, remove_left, remove_right)
            cache[(indices, start, end)] = min_result
            return min_result

        indices = tuple([i for i in range(len(s)) if s[i] == '1'])
        return min_time(indices, 0, len(s) - 1)

    def minimumTime(self, s: str) -> int:
        n = len(s)

        cost_left_to_right = [0] * n

        cost = 0 if s[0] == '0' else 1
        cost_left_to_right[0] = cost

        for i in range(1, n):
            if s[i] == '1':
                cost = min(cost + 2, i + 1)
            cost_left_to_right[i] = cost

        cost_right_to_left = [0] * n

        cost = 0 if s[-1] == '0' else 1
        cost_right_to_left[-1] = cost

        for i in range(n - 2, -1, -1):
            if s[i] == '1':
                cost = min(cost + 2, n - (i + 1) + 1)
            cost_right_to_left[i] = cost

        cost_right_to_left.append(0)

        min_cost = n
        for i in range(n):
            min_cost = min(min_cost, cost_left_to_right[i] + cost_right_to_left[i + 1])
        return min_cost


solution = Solution()
assert solution.minimumTime('1100101') == 5
assert solution.minimumTime('0010') == 2
assert solution.minimumTime("110001110000100001100010111101010011101101000111") == 40
