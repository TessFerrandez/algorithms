class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            result = ''
            for i in range(0, len(s), k):
                digits = [int(d) for d in s[i: i + k]]
                result += str(sum(digits))
            s = result
        return s


solution = Solution()
assert solution.digitSum(s="11111222223", k=3) == '135'
assert solution.digitSum(s="00000000", k=3) == '000'
