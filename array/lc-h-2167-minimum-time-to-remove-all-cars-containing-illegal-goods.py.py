class Solution:
    # based on janki vaghasiya
    def minimumTime1(self, s: str) -> int:
        n = len(s)

        cost_ltr = [0] * n
        cost_rtl = [0] * n

        # calculate cost left to right
        # either remove all elements before => cost = (i + 1)
        # or take the cost before and remove this as a middle => cost = [i - 1] + 2
        if s[0] == '1':
            cost_ltr[0] = 1

        for i in range(1, n):
            if s[i] == '1':
                cost_ltr[i] = min(cost_ltr[i - 1] + 2, i + 1)
            else:
                cost_ltr[i] = cost_ltr[i - 1]

        # calculate cost right to left
        # see left to right
        if s[n - 1] == '1':
            cost_rtl[n - 1] = 1

        for i in range(n - 2, -1, -1):
            if s[i] == '1':
                cost_rtl[i] = min(cost_rtl[i + 1] + 2, n - i)
            else:
                cost_rtl[i] = cost_rtl[i + 1]

        # calculate minimum cost
        minimum = min(cost_rtl[0], cost_ltr[n - 1])

        for i in range(n - 1):
            minimum = min(minimum, cost_ltr[i] + cost_rtl[i + 1])

        return minimum

    # based on Bakerston
    def minimumTime2(self, s: str) -> int:
        '''
        max_cost = remove all from middle = 2 * count('1')
        save_left = how much can we save by taking cars one by one from left
        save_right = how much can we save by taking cars one by one from right
        max_left = max save from left
        max_right = max save from right
        current_save = max_left[i] + max_right[i + 1]
        result = max_cost - max(current_save)
        '''
        n = len(s)

        if n == 1:
            return 1 if s == '1' else 0

        left_save = []
        current_save = 0

        for ch in s:
            current_save += 1 if ch == '1' else -1
            left_save.append(current_save)

        right_save = []
        current_save = 0
        for ch in s[::-1]:
            current_save += 1 if ch == '1' else -1
            right_save.append(current_save)
        right_save = right_save[::-1]

        max_cost = 2 * s.count('1')

        left_max, current = [left_save[0]], left_save[0]
        for i in range(1, n):
            current = max(current, left_save[i])
            left_max.append(current)

        right_max, current = [right_save[-1]], right_save[-1]
        for i in range(n - 2, -1, -1):
            current = max(current, right_save[i])
            right_max.append(current)
        right_max = right_max[::-1]

        max_save = 0
        for i in range(n - 1):
            max_save = max(max_save, max(0, left_max[i]) + max(0, right_max[i + 1]))

        return max_cost - max_save

    # based on DBabichev
    def minimumTime(self, s: str) -> int:
        '''
        the problem is finding the maximum sum of subarray or minimum sum of subarray

        1. Take some elements from the left
        2. Take some elements from the right
        3. Take the rest of the elements from the middle

        |..left..|..middle..|..right..|

        cost for left = len(left)
        cost for right = len(right)
        cost for middle = 2 * middle.count('1') = middle.count('1') + len(middle) - middle.count('0')
        total = len(left) + len(right) + len(middle) + middle.count('1') - middle.count('0')
              = len(s) + middle.count('1') - middle.count('0')

        so the problem is:
        find the sub array with the smallest middle.count('1') - middle.count('0')

        if we replace 0 with -1 - the problem is:
        find the sub array with the smallest sum (see problem 53)
        '''
        def minSum(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]

            for i in range(1, len(nums)):
                dp[i] = min(nums[i], nums[i] + dp[i - 1])

            return min(0, min(dp))

        n = len(s)
        s1 = [1 if i == '1' else -1 for i in s]
        score = minSum(s1)

        return n + score


solution = Solution()
assert solution.minimumTime('1100101') == 5
assert solution.minimumTime('0010') == 2
