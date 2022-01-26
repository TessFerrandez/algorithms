class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(original) -> str:
            result = ''
            for ch in original:
                if ch == "#":
                    result = result[:-1] if len(result) >= 1 else ''
                else:
                    result += ch
            return result

        return backspace(s) == backspace(t)


solution = Solution()
assert solution.backspaceCompare("ab#c", "ad#c")
assert solution.backspaceCompare("ab##", "c#d#")
assert not solution.backspaceCompare("a#c", "b")
