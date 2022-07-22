class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_string = str(num)
        count = 0
        for i in range(len(num_string) - k + 1):
            div = int(num_string[i: i + k])
            if div != 0 and num % div == 0:
                count += 1
        return count


solution = Solution()
assert solution.divisorSubstrings(240, 2) == 2
assert solution.divisorSubstrings(430043, 2) == 2
