class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        digits = [int(d) for d in list(s)]

        if max(digits) > k:
            return -1

        current = 0
        count = 1

        for digit in digits:
            if current * 10 + digit <= k:
                current = current * 10 + digit
            else:
                count += 1
                current = digit

        return count


solution = Solution()
assert solution.minimumPartition("165462", 60) == 4
assert solution.minimumPartition("238182", 5) == -1
