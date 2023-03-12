from collections import Counter, defaultdict
from functools import cache
from typing import List
from math import gcd, sqrt


def get_smallest_prime_factors():
    smallest_prime_factor = [i for i in range(MAX_VAL + 1)]

    for i in range(2, int(sqrt(MAX_VAL)) + 1):
        if smallest_prime_factor[i] == i:
            for j in range(i * i, MAX_VAL + 1, i):
                smallest_prime_factor[j] = min(smallest_prime_factor[j], i)

    return smallest_prime_factor


MAX_VAL = 10 ** 6
SMALLEST_PRIME_FACTOR = get_smallest_prime_factors()


class Solution:
    # TLE
    def findValidSplit_tle(self, nums: List[int]) -> int:
        current = 1
        prefix_prod = []

        for num in nums:
            current *= num
            prefix_prod.append(current)

        current = 1
        suffix_prod = []

        for num in nums[::-1]:
            current *= num
            suffix_prod.append(current)

        n = len(nums)
        for i in range(n - 1):
            if gcd(prefix_prod[i], suffix_prod[n - i - 2]) == 1:
                return i

        return -1

    # TLE
    # combining sieve with least common factor
    def findValidSplit_tle2(self, nums: List[int]) -> int:
        max_val = 10 ** 6 + 2
        prime = [True] * max_val
        prime[0] = prime[1] = False
        least_common_factor = [0] * max_val

        # calculate primes
        for i in range(2, max_val):
            if prime[i]:
                for j in range(2 * i, max_val, i):
                    prime[j] = False
                    if least_common_factor[j] == 0:
                        least_common_factor[j] = i

        @cache
        def get_prime_factors(num):
            factors = Counter()

            if prime[num]:
                factors[num] += 1
            else:
                while num != 1:
                    if least_common_factor[num] == 0:
                        divisor = num
                    else:
                        divisor = least_common_factor[num]
                    factors[divisor] += 1
                    num //= divisor

            return factors

        def common_factors(factors1, factors2):
            for factor in factors2:
                if factors1[factor] and factors2[factor]:
                    # some common factors, so not a valid split
                    return False
            return True

        suffix_factors = Counter()

        def fill_suffix_factors():
            for num in nums:
                if prime[num]:
                    suffix_factors[num] += 1
                else:
                    factors = get_prime_factors(num)
                    for factor in factors:
                        suffix_factors[factor] += factors[factor]

        fill_suffix_factors()
        prefix_factors = Counter()

        for split_idx, num in enumerate(nums[:-1]):
            factors = get_prime_factors(num)

            # move the factors of the current number
            # from the suffix to the prefix
            for factor in factors:
                prefix_factors[factor] += factors[factor]
                suffix_factors[factor] -= factors[factor]

            if common_factors(prefix_factors, suffix_factors):
                return split_idx

        return -1

    # requires pre-calculated smallest-prime-factor
    def findValidSplit(self, nums: List[int]) -> int:
        @cache
        def get_prime_factors(num):
            factors = []
            while num != 1:
                factors.append(SMALLEST_PRIME_FACTOR[num])
                num //= SMALLEST_PRIME_FACTOR[num]
            return factors

        factor_index = defaultdict(int)
        for idx, num in enumerate(nums):
            for factor in get_prime_factors(num):
                factor_index[factor] = idx

        right_most = 0
        for idx in range(len(nums) - 1):
            for factor in get_prime_factors(nums[idx]):
                right_most = max(right_most, factor_index[factor])
            if right_most == idx:
                return idx

        return -1


solution = Solution()
assert solution.findValidSplit([4,7,8,15,3,5]) == 2
assert solution.findValidSplit([4,7,15,8,3,5]) == -1
