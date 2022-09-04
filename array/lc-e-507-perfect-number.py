from math import sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        def get_divisors(num):
            divisors = []

            # Note that this loop runs till square root
            i = 1
            while i <= sqrt(num):
                if num % i == 0:
                    if (num / i == i):
                        divisors.append(i)
                    else:
                        divisors.append(i)
                        divisors.append(num // i)
                i = i + 1
            return divisors

        divisors = get_divisors(num)

        return num == sum(div for div in divisors if div != num)


solution = Solution()
assert solution.checkPerfectNumber(28)
assert not solution.checkPerfectNumber(7)
