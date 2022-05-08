class Solution:
    # O(n), O(n)
    def removeDuplicates1(self, s: str, k: int) -> str:
        stack = []
        freq = []

        for ch in s:
            if stack and ch == stack[-1]:
                if freq[-1] == k - 1:
                    for _ in range(k - 1):
                        stack.pop()
                    freq.pop()
                else:
                    stack.append(ch)
                    freq[-1] += 1
            else:
                stack.append(ch)
                freq.append(1)

        return ''.join(stack)

    # O(n), O(n) - but better avg/min
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []      # [[char, frequency]...]

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])

        return ''.join([ch * freq for ch, freq in stack])


solution = Solution()
assert solution.removeDuplicates('abcd', 2) == 'abcd'
assert solution.removeDuplicates('deeedbbcccbdaa', 3) == 'aa'
assert solution.removeDuplicates('pbbcggttciiippooaais', 2) == 'ps'
