from collections import defaultdict


def basics(a, b):
    print(f"{a} = {bin(a)[2:]}, {b} = {bin(b)[2:]}")
    print("SET UNION:\t", a | b, bin(a | b)[2:])
    print("SET INTERSECT:\t", a & b, bin(a & b)[2:])
    print("SET SUBTRACT:\t", a & ~b, bin(a & ~b)[2:])
    print("SET NEGATE:\t", ~a, bin(~a))

    bit = 2
    print("SET BIT:\t", a | 1 << bit, bin(a | 1 << bit)[2:])
    print("TEST BIT:\t", (a & 1 << bit) != 0)
    print("EXTRACT LAST BIT:\t", a & -a)
    print("REMOVE LAST BIT:\t", a & (a - 1), bin(a & (a - 1))[2:])
    print("GET ALL 1-bits:\t", ~0, bin(~0)[2:])


def count_ones(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count


def is_power_of_four(n):
    return (n & (n - 1)) == 0 and (n & 0x55555555) != 0


def get_sum(a, b):
    return a if b == 0 else get_sum(a ^ b, (a & b) << 1)


def missing_number(nums):
    result = 0
    for i, num in enumerate(nums):
        result ^= i
        result ^= nums[i]

    result ^= len(nums)
    return result


def largest_power(n):
    '''largest power of 2 less than n'''
    n |= (n >> 1)
    n |= (n >> 2)
    n |= (n >> 4)
    n |= (n >> 8)
    n |= (n >> 16)
    return (n + 1) >> 1


def reverse_bits1(n):
    mask = 1 << 31
    result = 0

    for _ in range(32):
        if n & 1:
            result |= mask
        mask >>= 1
        n >>= 1
    return result


def reverse_bits2(n):
    mask, result = 1, 0
    for _ in range(32):
        result <<= 1
        if mask & n:
            result |= 1
        mask <<= 1
    return result


def reverse_bits(x):
    x = ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1)
    x = ((x & 0xcccccccc) >> 2) | ((x & 0x33333333) << 2)
    x = ((x & 0xf0f0f0f0) >> 4) | ((x & 0x0f0f0f0f) << 4)
    x = ((x & 0xff00ff00) >> 8) | ((x & 0x00ff00ff) << 8)
    x = ((x & 0xffff0000) >> 16) | ((x & 0x0000ffff) << 16)
    return x


def range_bitwise_and(m, n):
    '''
    Given a range [m, n] - return the bitwise and of all numbers in the range
    ex [5, 7] = 101 & 110 & 111 => 100 = 4

    5 = 101 => 10 => 1
    7 = 111 => 11 => 1
    shift   => 1  => 2
    result = 100
    '''
    shift = 0
    while m != n:
        m >>= 1
        n >>= 1
        shift += 1
    return m << shift


def hamming_weight(n):
    ''' number of 1 bits '''
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count

# APPLICATIONS
# ------------
def find_repeated_dna_sequences(s):
    '''
    Given a string s with ACGT ex. ACGAATTCCG
    Find any 10 char long sequences that occur more than once in the DNA
    '''
    n = len(s)

    if n < 11:
        return []

    results = []
    keymap = defaultdict(int)

    # hash first chars
    hash_key = 0
    for i in range(9):
        hash_key = (hash_key << 2) | (ord(s[i]) - 65 + 1) % 5

    for i in range(9, len(s)):
        hash_key = ((hash_key << 2) | (ord(s[i]) - 65 + 1) % 5) & 0xfffff
        keymap[hash_key] += 1
        if keymap[hash_key] == 2:
            results.append(s[i - 9: i + 1])

    return results


def find_majority_element(nums):
    n = len(nums)
    count, mask, result = 0, 1, 0
    for _ in range(32):
        count = 0
        for j in range(n):
            if mask & nums[j]:
                count += 1
        if count > n // 2:
            result |= mask
        mask <<= 1
    return result


def single_number_iii(nums):
    '''
    every number appears 3 times except for one - find that one
    a = a & ~b & ~c + ~a & b & c
    b = ~a & b & ~c + ~a & ~b & c
    return a | b since the single number can appear once or twice
    '''
    temp = a = b = 0
    for i in range(len(nums)):
        temp = (a & ~b & ~nums[i]) | (~a & b & nums[i])
        b = (~a & b & ~nums[i]) | (~a & ~b & nums[i])
        a = temp
    return a | b


def max_product(words):
    '''
    Given a list of words  ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    return the max value of len(word[i]) * len(word[j]) where word[i] and word[j] do not share any letters.
    Return 0 if no such words exist

    Restrictions: The words only contains lower case letters

    Solution: for each word, mark all characters with a 1 bit
    check if two words contain the same chars by and-ing them
    '''
    lens = [len(word) for word in words]
    masks = [0] * len(words)

    result = 0
    for i in range(len(words)):
        for ch in words[i]:
            masks[i] |= 1 << (ord(ch) - ord('a'))
        for j in range(i):
            if (masks[i] & masks[j]) == 0:
                result = max(result, lens[i] * lens[j])

    return result


'''
it is trivial to iterate over subsets of an n-element set
if a is a subset of b, then the number representing a < b

it is also possible to iterate over all subsets of a particular subest (repr by a bit pattern)
provided it is ok to visit them backwards
'''
def subsets(nums):
    n = len(nums)

    if n == 0:
        return []

    num = 1 << n
    results = [[] for _ in range(num)]
    for i in range(num):
        for j in range(n):
            if ((1 << j) & i):
                results[i].append(nums[j])

    return results


# basics(11, 6)
assert count_ones(11) == 3              # 1011
assert count_ones(6) == 2               # 1010
assert is_power_of_four(4)
assert not is_power_of_four(5)
assert is_power_of_four(16)
assert get_sum(7, 6) == 13
assert missing_number([0, 1, 3]) == 2
assert largest_power(7) == 4
assert reverse_bits(13) == 2952790016   # 1101 -> 10110000...00
assert range_bitwise_and(5, 7) == 4
assert hamming_weight(11) == 3

# APPLICATIONS
assert find_repeated_dna_sequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT') == ["AAAAACCCCC", "CCCCCAAAAA"]
assert find_majority_element([1, 2, 2, 1, 1, 2, 2]) == 2
assert single_number_iii([1, 2, 1, 1, 2, 3, 2]) == 3
assert max_product(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
assert max_product(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
assert max_product(["a", "aa", "aaa", "aaaa"]) == 0
print(subsets([1, 2, 3, 4, 5]))
