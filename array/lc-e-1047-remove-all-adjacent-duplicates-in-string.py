class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []

        for ch in s:
            if result and result[-1] == ch:
                result.pop()
            else:
                result.append(ch)

        return ''.join(result)


solution = Solution()
assert solution.removeDuplicates('abbaca') == 'ca'
assert solution.removeDuplicates('azxxzy') == 'ay'
