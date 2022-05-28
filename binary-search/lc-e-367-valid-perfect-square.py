class Solution:
    # in order from worst to best
    # brute force (17.6)
    def isPerfectSquare1(self, num: int) -> bool:
        for i in range(num + 1):
            if i ** 2 == num:
                return True
        return False

    # math (2.64)
    def isPerfectSquare2(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

    # binary search (1.5)
    def isPerfectSquare3(self, num: int) -> bool:
        low, high = 0, num

        while low <= high:
            mid = (low + high) // 2
            pow2 = mid * mid
            if pow2 == num:
                return True
            if pow2 < num:
                low = mid + 1
            else:
                high = mid - 1

        return False

    # binary template
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 0, num

        while low < high:
            mid = (low + high) // 2
            if mid * mid == num:
                return True
            if mid * mid >= num:
                high = mid
            else:
                low = mid + 1

        return low * low == num

    # bitwise (0.45)
    def isPerfectSquare4(self, num: int) -> bool:
        root = 0
        bit = 1 << 15

        while bit > 0:
            root |= bit
            if root > num // root:
                root ^= bit
            bit >>= 1
        return root * root == num

    # newton (0.34)
    def isPerfectSquare5(self, num: int) -> bool:
        r = num
        while r * r > num:
            r = (r + num / r) // 2
        return r * r == num


solution = Solution()
assert solution.isPerfectSquare(1)
assert solution.isPerfectSquare(16)
assert not solution.isPerfectSquare(14)
