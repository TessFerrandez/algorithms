class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                substr_rev = ''
                while stack[-1] != '[':
                    substr_rev += stack.pop()
                stack.pop()

                num_rev = ''
                while stack and '0' <= stack[-1] <= '9':
                    num_rev += stack.pop()
                num = int(''.join(reversed(num_rev)))

                sub_str = num * ''.join(reversed(substr_rev))
                for ch in sub_str:
                    stack.append(ch)
            else:
                stack.append(ch)
        result = ''.join(stack)
        return result


solution = Solution()
assert solution.decodeString('3[a2[c]]') == 'accaccacc'
assert solution.decodeString('3[a]2[bc]') == 'aaabcbc'
